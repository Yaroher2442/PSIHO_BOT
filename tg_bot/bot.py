import threading

import telebot
from config.conf import Configurator
from tg_bot.BotLogic import BotUseLogic
from tg_bot.BotLogic import Answer
conf = Configurator()


class TGBot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.db = BotUseLogic()
        self.bot = telebot.TeleBot(conf.tg_conf.token)

        @self.bot.message_handler(commands=['start'])
        def init(message):
            answr = Answer(message)
            self.bot.send_message(message.from_user.id, answr.returns_answr, answr.reply_markup)

        @self.bot.message_handler()
        def init(message):
            pass

    def run(self):
        self.bot.infinity_polling(True)


# @tg_bot.message_handler()
# def start(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_start = types.KeyboardButton(text="Начать!")
#     keyboard.add(button_start)
#     if (message.text == '/start' or message.text == 'Вернуться в меню ⬅️'):
#         keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#         button_psycho = types.KeyboardButton(text="Психосоматика")
#         button_meditation = types.KeyboardButton(text="Медитации")
#         button_youtube = types.KeyboardButton(text="Ютуб канал")
#         button_telegram = types.KeyboardButton(text="Канал Центра в Телеграме")
#         button_institute = types.KeyboardButton(text="Институт психосоматики")
#         button_appointment = types.KeyboardButton(text="Запись на консультацию")
#         keyboard.add(button_psycho, button_meditation, button_youtube, button_telegram, button_institute,
#                      button_appointment)
#         tg_bot.send_message(message.from_user.id, 'Выберите одно из предложенных действий', reply_markup=keyboard)
#

if __name__ == '__main__':
    bot_worker = TGBot()
    bot_worker.setDaemon(True)
    bot_worker.start()
    bot_worker.join()
    # tg_bot.infinity_polling(True)
