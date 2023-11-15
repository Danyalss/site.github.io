from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', style_sheet='style.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
