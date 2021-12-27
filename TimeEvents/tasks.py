import datetime

from loguru import logger

from TimeEvents.context import NotifyTaskContext


class TaskStatus:
    done = "done"
    run = "running"
    pending = "pending"
    canceled = "canceled"


class Task:
    id_: int
    deferre_time: datetime.datetime
    status = str


class NotifyTaskWorker(Task):
    def __init__(self, id_, context: NotifyTaskContext):
        self.id_ = id_
        self.status = TaskStatus.pending
        self.context = context
        self.exceptions = 0

    def payload(self):
        return self.context.payload

    async def action(self, users):
        self.status = TaskStatus.run
        for user in users:
            if self.status != TaskStatus.canceled:
                try:
                    self.context.bot.send_message(user.tg_id, self.context.notification)
                except Exception as e:
                    logger.warning(f"Can't send notify to {user.username}, cause: {e} in task {self}")
                    self.exceptions += 1
        self.context.payload = {
            "message": f"{len(users) - self.exceptions} из {len(users)} пользователей получили сообщения, остальные заблокировали бота"}
        self.status = TaskStatus.done
