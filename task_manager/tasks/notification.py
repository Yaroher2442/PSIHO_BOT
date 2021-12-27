from time import sleep

from loguru import logger
from task_manager.context.notify_context import NotifyContext
from task_manager.tasks.task import Task, TaskStatus


class NotifyTask(Task):
    def __init__(self, context: NotifyContext, name: str):
        super().__init__(context)
        self.bot = self.context.bot

    async def perform(self):
        sleep(2)
        logger.debug("mew bot = asfasfasf")
        self.status = TaskStatus.SUCCESS
