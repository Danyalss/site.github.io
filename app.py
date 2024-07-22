import os
from telebot import TeleBot, types

    # # pip install python-dotenv
    # from dotenv import load_dotenv



# دریافت توکن ربات از متغیرهای محیطی
BOT_TOKEN = '7477026941:AAHzwdrmHfSX25w-DgQ2nnCinVd7af8sZ8I'

bot = TeleBot(BOT_TOKEN)

# ویدئو ثابت
VIDEO_PATH = 'vid.mp4'

# لینک آپلود شده ویدئو
uploaded_video_id = 'BAACAgQAAxkDAAMHZp679V6OZLA4aKjc4bJ3x0HzSL8AAtQVAAKqBPlQxhJN7Q3FG0M1BA'

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global uploaded_video_id

    # افزودن نام کاربر به توضیحات
    user_first_name = message.from_user.first_name
    description = f"سلام {user_first_name}! . \n اینجا صدیقی کوین عه و دانیال بیکار اینو ساخته و خودشم نمی دونه جرا ساخته ولی خوب ... "

    # ایجاد دکمه شیشه‌ای
    markup = types.InlineKeyboardMarkup()
    web_app_info = types.WebAppInfo(url='https://danyalss.github.io/site.github.io')
    button = types.InlineKeyboardButton(text="ورود به صدیقی کوین 🎨", web_app=web_app_info)
    markup.add(button)

    if uploaded_video_id is None:
        with open(VIDEO_PATH, 'rb') as video:
            msg = bot.send_video(message.chat.id, video, caption=description, reply_markup=markup)
            uploaded_video_id = msg.video.file_id
            print(f'Uploaded video ID: {uploaded_video_id}')
    else:
        bot.send_video(message.chat.id, uploaded_video_id, caption=description, reply_markup=markup)

bot.polling()