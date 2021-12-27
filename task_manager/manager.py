import asyncio
import threading
from typing import List

from task_manager.tasks.notification import NotifyTask
from task_manager.tasks.task import Task, TaskStatus
from loguru import logger
from task_manager.context.notify_context import NotifyContext


class TaskManager(threading.Thread):
    def __init__(self):
        super().__init__()
        logger.debug("thread start")
        self.tasks_list: List[Task] = []
        self.loop = asyncio.get_event_loop()

    def set_task(self, task: Task):
        self.tasks_list.append(task)

    async def idle(self):
        for task in self.tasks_list:
            logger.debug(task)
            logger.debug(task.status)
            if task.status == TaskStatus.PENDING:
                await task.verify()
            if task.status == TaskStatus.READY:
                await task.run()
            if task.status == TaskStatus.SUCCESS:
                logger.debug(f"task {task} complite")
                self.tasks_list.pop(self.tasks_list.index(task))
        logger.debug("call tasks ")

    def run(self):
        while True:
            self.loop.run_until_complete(self.idle())


if __name__ == '__main__':
    tm = TaskManager()
    tm.setDaemon(True)
    tm.start()
    cotext = NotifyContext(bot="asfasfasf")
    tm.set_task(NotifyTask(cotext, "Asfasfasf"))
    tm.join()
