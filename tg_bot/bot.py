import threading
import telebot
from tg_bot.BotLogic import Answer
from config.loger import AppLogger


class TGBot(threading.Thread):
    def __init__(self, conf):
        threading.Thread.__init__(self)
        self.bot = telebot.TeleBot(conf.tg_conf.token)
        self.logger = AppLogger("bot.", conf)

        @self.bot.message_handler()
        def init(message):
            answr = Answer(message, self.logger)
            self.bot.send_message(message.from_user.id, answr.returns_answr, reply_markup=answr.reply_markup,
                                  parse_mode="html")

    def run(self):
        self.logger.debug("Bot started")
        self.bot.infinity_polling(True)
