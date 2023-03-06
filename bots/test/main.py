import telebot

from decouple import config
token = config('TOKEN')


bot =telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBSVkBXYWHKNLTkgl7URRSdeSiaNX2wACRhcAApdF6UvO9wLFTXTONi4E')
    bot.send_photo(message.chat.id, 'https://img.freepik.com/premium-vector/robot-icon-bot-sign-design-chatbot-symbol-concept-voice-support-service-bot-online-support-bot-vector-stock-illustration_100456-34.jpg')
@bot.message_handler(content_types=['text'])   
def aaaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    else:
        bot.send_message(message.chat.id, 'Сообщение не распознанно')

@bot.message_handler(content_types=['sticker'])
def bbbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)


bot.polling()
