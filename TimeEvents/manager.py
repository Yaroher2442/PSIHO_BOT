import asyncio
import datetime
import threading
from time import sleep
from typing import List

from telegram.ext import ExtBot

from TimeEvents.context import NotifyTaskContext
from TimeEvents.tasks import Task, TaskStatus, NotifyTaskWorker
from config_.conf import Configurator
from config_.loger import app_logger
from database.DB_interface import DBInterface
from database.models import NotifyTask


class Manager(threading.Thread):
    def __init__(self,conf:Configurator, bot: ExtBot):
        super().__init__()
        self.conf=conf
        self.bot = bot
        self.db = DBInterface()
        self.ioloop = asyncio.get_event_loop()
        self.task_in_run: List[NotifyTaskWorker] = []

    async def get_db_tasks(self) -> List[NotifyTask]:
        return self.db.NotifyTasks.get_all().where(
            (self.db.NotifyTasks.table.status != TaskStatus.done) & (
                    self.db.NotifyTasks.table.status != TaskStatus.canceled)
            & (self.db.NotifyTasks.table.status != TaskStatus.run))

    async def update_users(self):
        return self.db.get_users()

    def complete_task_db(self, task):
        self.db.NotifyTasks.update(task.id_, status=TaskStatus.done)
        self.db.NotifyTasks.update(task.id_, message=task.payload()["message"])

    def run_task_db(self, id_):
        self.db.NotifyTasks.update(id_, status=TaskStatus.run)


    async def looper(self):
        while True:
            completed_task = []
            for task in self.task_in_run:
                if task.status == TaskStatus.done:
                    self.complete_task_db(task)
                    completed_task.append(task)
            for t in completed_task:
                self.task_in_run.pop(self.task_in_run.index(t))
            new_tasks = await self.get_db_tasks()
            for task in new_tasks:
                context = NotifyTaskContext(self.bot, task.notify)
                worker = NotifyTaskWorker(task.id, context)
                if task.deferre_time <= datetime.datetime.now():
                    self.task_in_run.append(worker)
                app_logger.debug(worker)
            users = await self.update_users()
            for worker in self.task_in_run:
                asyncio.ensure_future(worker.action(users))
                self.run_task_db(worker.id_)
            await asyncio.sleep(self.conf.timer_conf.timeout)

    def run(self):
        self.ioloop.run_until_complete(self.looper())
