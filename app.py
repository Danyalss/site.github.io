import os
from telebot import TeleBot, types
import pickle


    # # pip install python-dotenv
    # from dotenv import load_dotenv

def save_user_ids(user_ids):
    with open('backup/user_ids.pickle', 'wb') as handle:
        pickle.dump(user_ids, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_user_ids():
    try:
        with open('backup/user_ids.pickle', 'rb') as handle:
            user_ids = pickle.load(handle)
            return user_ids
    except FileNotFoundError:
        return []

load_user_ids()


# دریافت توکن ربات از متغیرهای محیطی
BOT_TOKEN = '7477026941:AAHzwdrmHfSX25w-DgQ2nnCinVd7af8sZ8I'

bot = TeleBot(BOT_TOKEN)
admin_id = 1663788795
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

    chat_id = message.chat.id

    # ذخیره آیدی عددی کاربر
    user_ids = load_user_ids()
    if chat_id not in user_ids:
        global new_users
        user_ids.append(chat_id)
        save_user_ids(user_ids)


        # ارسال جزئیات کاربر جدید به مدیر
        user_details = f"🍔 کاربر جدید {chat_id} به ربات اضافه شد.\n\n"
        user_details += f"ایدی عددی کاربر: {chat_id}\n"
        user_details += f"نام: {message.from_user.first_name if message.from_user.first_name else 'نامشخص'}\n"
        user_details += f"نام خانوادگی: {message.from_user.last_name if message.from_user.last_name else 'نامشخص'}\n"

        if message.from_user.username:
            user_details += f"یوزرنیم: @{message.from_user.username}"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Go to chat", url=f"https://t.me/{message.from_user.username}"))
            bot.send_message(admin_id, user_details, reply_markup=markup)
        else:
            user_details += f"🔥 User ID: [{message.from_user.id}](tg://user?id={message.from_user.id})"
            bot.send_message(admin_id, user_details, parse_mode='Markdown', disable_web_page_preview=True)

        new_users += 1


bot.polling()