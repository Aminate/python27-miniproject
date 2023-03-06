import telebot
from decouple import config



token = config('TOKEN')
#стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBW5kBYbQ08iWUanhn-Nvy59HyxAXfAACEwADwDZPE6qzh_d_OMqlLgQ'
no_sticker = 'CAACAgIAAxkBAAEIBXxkBYbdwMjR9yGSlRxfm4jvxntX2wACDgADwDZPEyNXFESHbtZlLgQ'

#клавиатура под сообщением

keyboard= telebot.types.InlineKeyboardMarkup()    #эти кнопки за нас не пишут
b1 = telebot.types.InlineKeyboardButton('ДА', callback_data='yes')
b2 =telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(b1,b2)





bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет,хочешь поговорить?', reply_markup=keyboard)


#func - это функция фильтр, в данном случае разрешаются все сообщение
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)







bot.polling()   #запускает нашего бота