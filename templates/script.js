let tg = {
    token: "6583320212:AAGci8mHu1_ctX1OIQd2rlvqHM-11FIGsZ4", // توکن ربات خود را از @BotFather دریافت کنید
    chat_id: "1663788795" // شناسه چت کاربری که می‌خواهید به آن پیام ارسال کنید
  }
  
  function sendMessage (text) {
    const url = `https://api.telegram.org/bot${tg.token}/sendMessage`; // URL درخواست
    const obj = {
      chat_id: tg.chat_id, // شناسه چت تلگرام
      text: text // متن برای ارسال
    };
  
    const xht = new XMLHttpRequest();
    xht.open("POST", url, true);
    xht.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xht.send(JSON.stringify(obj));
  }
  