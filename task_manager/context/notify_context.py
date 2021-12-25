from task_manager.context.context import TaskContext


class NotifyContext(TaskContext):
    bot: str = None

    def __init__(self, bot: str):
        self.bot = bot
