import os
from telebot import TeleBot
from telebot.types import InputFile

    # # pip install python-dotenv
    # from dotenv import load_dotenv



# دریافت توکن ربات از متغیرهای محیطی
BOT_TOKEN = '7477026941:AAHzwdrmHfSX25w-DgQ2nnCinVd7af8sZ8I'

bot = TeleBot(BOT_TOKEN)

# ویدئو ثابت
VIDEO_PATH = 'vid.mp4'

# لینک آپلود شده ویدئو
uploaded_video_id = None

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global uploaded_video_id
    
    # افزودن نام کاربر به توضیحات
    user_first_name = message.from_user.first_name
    description = f"سلام {user_first_name}! . \n اینجا صدیقی کوین عه و دانیال بیکار اینو ساخته و خودشم نمی دونه جرا ساخته ولی خوب ... "
    

    if uploaded_video_id is None:
        with open(VIDEO_PATH, 'rb') as video:
            msg = bot.send_video(message.chat.id, video, caption=description)
            uploaded_video_id = msg.video.file_id
            print(f'Uploaded video ID: {uploaded_video_id}')
    else:
        bot.send_video(message.chat.id, uploaded_video_id, caption=description)

bot.polling()
