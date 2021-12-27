from typing import List
from telegram.ext import ExtBot


class Context:
    def __init__(self):
        pass


class NotifyTaskContext(Context):
    bot: ExtBot
    notification: str

    def __init__(self, bot: ExtBot, notification: str):
        super(NotifyTaskContext, self).__init__()
        self.bot = bot
        self.notification = notification
        self.payload = {}
