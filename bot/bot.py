from telebot import types
import telebot
import json
from config.conf import Configurator

conf = Configurator()

bot = telebot.TeleBot(conf.tg_conf.token)


@bot.message_handler()
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_start = types.KeyboardButton(text="Начать!")
    keyboard.add(button_start)
    if (message.text == '/start' or message.text == 'Вернуться в меню ⬅️'):
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_psycho = types.KeyboardButton(text="Психосоматика")
        button_meditation = types.KeyboardButton(text="Медитации")
        button_youtube = types.KeyboardButton(text="Ютуб канал")
        button_telegram = types.KeyboardButton(text="Канал Центра в Телеграме")
        button_institute = types.KeyboardButton(text="Институт психосоматики")
        button_appointment = types.KeyboardButton(text="Запись на консультацию")
        keyboard.add(button_psycho, button_meditation, button_youtube, button_telegram, button_institute,
                     button_appointment)
        bot.send_message(message.from_user.id, 'Выберите одно из предложенных действий', reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling(True)
