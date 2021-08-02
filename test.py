from telebot import types
import telebot

from datetime import datetime

bot = telebot.TeleBot("1709972597:AAGadK_mJ4fu6vsAANDL_Tt1dN8HDRC1J58")


@bot.message_handler()
def get_start(message):
    print(message.date)
    dt_object = datetime.fromtimestamp(message.date)
    print("dt_object =", dt_object)
    print("type(dt_object) =", type(dt_object))


if __name__ == '__main__':
    bot.infinity_polling(True)
