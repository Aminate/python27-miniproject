import telebot
from decouple import config



token = config('TOKEN')
#стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBW5kBYbQ08iWUanhn-Nvy59HyxAXfAACEwADwDZPE6qzh_d_OMqlLgQ'
no_sticker = 'CAACAgIAAxkBAAEIBXxkBYbdwMjR9yGSlRxfm4jvxntX2wACDgADwDZPEyNXFESHbtZlLgQ'


bot = telebot.TeleBot(token)

#клавиатура
keyboart = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('Конечно')
b2 = telebot.types.KeyboardButton('Не особа')
keyboart.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет,хочешь поговорить?', reply_markup=keyboart)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Конечно':
        bot.send_sticker(message.chat.id,yes_sticker)
    elif message.text == 'Не особа':
         bot.send_sticker(message.chat.id,no_sticker)
    else:
        bot.send_message(message.chat.id, 'ВЫБЕРИ ЧТО-ТО С КНОПКИ!')

    bot.register_next_step_handler(message, reply_to_button)    






bot.polling()   #запускает нашего бота