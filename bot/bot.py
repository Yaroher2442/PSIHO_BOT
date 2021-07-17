from telebot import types
import telebot
import json
from config.conf import Configurator

conf = Configurator()

bot = telebot.TeleBot(conf.tg_conf.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "")


if __name__ == '__main__':
    bot.infinity_polling(True)
