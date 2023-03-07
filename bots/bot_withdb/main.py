import telebot
from decouple import config
from buttons import keyboard
from utils import get_db   #импорт база данных


token = config("TOKEN")

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Как оно?", reply_markup=keyboard)

@bot.callback_query_handler(lambda x:True) #фильтр дает добро

def send_data(call):
    db = get_db()
    page = call.data
    products = db[page]
    for prod in products:    #проходимся по баз.данных
        text = f"""
        Title:{prod['title']}
        Price:{prod['price']}
        """
        bot.send_message(call.from_user.id, text)


bot.polling()