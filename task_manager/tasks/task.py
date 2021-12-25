import asyncio
from enum import Enum
from uuid import uuid4
from loguru import logger

from task_manager.context.context import TaskContext


class TaskStatus(Enum):
    PENDING = 0
    READY = 1
    RUN = 2
    SUCCESS = 3
    WARNING = 4
    ERROR = 5


class Task:
    def __init__(self, context: TaskContext, name: str = None):
        self.context = context
        self.name = name
        self.id = uuid4()
        self.status: TaskStatus = TaskStatus.PENDING

    async def verify(self, *args, **kwargs):
        logger.debug(f"verify {self.name}")
        self.status = TaskStatus.READY

    async def run(self):
        if self.status == TaskStatus.READY:
            self.status = TaskStatus.RUN
        await self.perform()

    async def perform(self):
        logger.debug("perform")

    def __repr__(self):
        return f'<{self.__class__.__module__}.{self.__class__.__name__}:{self.name} id: {self.id} object at {hex(id(self))}>'
