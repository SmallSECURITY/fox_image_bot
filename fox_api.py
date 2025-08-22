from telebot import TeleBot
from requests import get
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton 


API_TOKEN = ""

bot = TeleBot(API_TOKEN)

key = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton("🦊 روباه رندوم", callback_data="get_fox")
key.add(btn1)

@bot.message_handler(commands=["start"])
def start_bot(message):


    bot.send_message(chat_id= message.chat.id , text="به ربات ما خوش آمدید\nبرای دریافت عکس روباه از دکمه پایین استفاده کنید",reply_markup=key)

@bot.callback_query_handler(func= lambda call:True)
def api_fox(call):
    if call.data == "get_fox":
        url_fox = get("https://randomfox.ca/floof/")
        get_image = url_fox.json()
        image_url = get_image["image"]
        bot.send_photo(chat_id=call.message.chat.id , photo=image_url, caption="🦊 روباه رندوم", reply_markup=key)


    else:
        bot.send_message(chat_id= call.message.chat.id , text="پیغام شما برای من تعریف نشده", reply_markup=key)
    
bot.polling(non_stop=True)