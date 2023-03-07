import telebot

# bot = telebot.TeleBot('6016183586:AAE1AsR-a5WGzRSasr0RPIOIuplKtVYevlc')
token = '6016183586:AAE1AsR-a5WGzRSasr0RPIOIuplKtVYevlc'
bot = telebot.TeleBot(token)
# @bot.message_handler(commands=['start'])
# def start(message):



# Всем добра! Помогите! При созданий телеграмм бота выдает такую ошибку при запуске с командной строки! Вот код:

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, message.text)

bot.polling( none_stop = True)