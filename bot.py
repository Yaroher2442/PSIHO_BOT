from telebot import types
import telebot
import json

with open('config.json')  as conf_file:
    token = json.load(conf_file)['telegram_token']

print(token)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "")


if __name__ == '__main__':
    bot.infinity_polling(True)
