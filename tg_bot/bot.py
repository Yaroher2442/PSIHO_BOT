import threading
import telebot
# from tg_bot.BotLogic import Answer
from tg_bot.AnswerClass import Answer
from config.loger import AppLogger

class TGBot(threading.Thread):
    def __init__(self, conf):
        threading.Thread.__init__(self)
        self.bot = telebot.TeleBot(conf.tg_conf.token)
        self.logger = AppLogger("bot", conf)

        @self.bot.message_handler()
        def init(message):
            answr = Answer(message, self.logger)
            self.logger.info(answr.__dict__)
            answr.send_message(self.bot)

    def run(self):
        self.logger.debug("Bot started")
        self.bot.infinity_polling(True)


