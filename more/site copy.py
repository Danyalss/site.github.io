from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, unquote
import urllib.request

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_GET(self, body=True):
        url = parse_qs(urlparse(self.path).query).get('target', None)
        if url is None:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Target parameter missing')
            return
        url = unquote(url[0])
        self.send_response(200)
        try:
            with urllib.request.urlopen(url) as target:
                self.send_response(target.getcode())
                self.send_header('Content-Type', target.info().get_content_type())
                self.end_headers()
                if body:
                    self.wfile.write(target.read())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    do_HEAD = do_GET
    do_POST = do_GET
    do_PUT = do_GET
    do_DELETE = do_GET

httpd = HTTPServer(('localhost', 8000), ProxyHTTPRequestHandler)
print('Proxy server listening on port 8000')
httpd.serve_forever()
