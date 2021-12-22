import threading
from time import sleep

from loguru import logger
from telegram import Update, Chat, ChatMember, ParseMode, ChatMemberUpdated
# from tg_bot.BotLogic import Answer
from telegram.ext import MessageHandler, Updater, CallbackContext, BaseFilter, Dispatcher, ExtBot

# from tg_bot.AnswerClass import Answer
from config_.loger import AppLogger
from tg_bot.AnswerClass import Answer


class TGBot(threading.Thread):
    def __init__(self, conf):
        threading.Thread.__init__(self)
        self.updater: Updater = Updater(conf.tg_conf.token)
        self.bot: ExtBot = self.updater.bot

        self.dispatcher: Dispatcher = self.updater.dispatcher
        self.setup_handlers()

        self.logger = AppLogger("bot", conf)

    # def send_notifys(self):
    #     self.updater.bot.se
    def message_handle(self, update: Update, context: CallbackContext):
        self.logger.debug(update.message)
        answr = Answer(update.message, self.logger)
        answr.send_message(context)
        # context.bot.send_message(update.message.chat_id,"привет")

    def setup_handlers(self):
        self.dispatcher.add_handler(MessageHandler(None, callback=self.message_handle))

    def run(self) -> None:
        self.logger.debug("Bot started")
        while True:
            if not self.is_alive():
                self.start()
            self.updater.start_polling(drop_pending_updates=True)
            sleep(0.4)
