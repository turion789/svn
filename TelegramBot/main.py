import telebot

#import json


api_token = '6278534543:AAEJXvSs4B4z_emu7H1095iPGdg4We5DjtE'

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])   # команда
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}') #тут можно парсить

@bot.message_handler(commands=['help'])   # команда
def main(message):
    bot.send_message(message.chat.id, '<b>Привет</b> <em><u>https://www.youtube.com</u></em>', parse_mode='html')

bot.polling(none_stop=True)
