from typing import Annotated

from aiogram import Dispatcher, Router, types
from aiogram.filters.command import Command

from aiogram_dialog import Dialog, DialogManager, LaunchMode, StartMode, Window
from aiogram_dialog.widgets.text import Format

from dishka.integrations.aiogram import Depends, inject

from services.compliments import Compliments

from .states import CountGroup


class CountDialog:
    _compliments_count: int = 0

    @classmethod
    @inject
    async def count_handler(
            cls, message: types.Message,
            dialog_manager: DialogManager,
            compliments: Annotated[Compliments, Depends()],
    ):
        cls._compliments_count = len(compliments.data)
        await dialog_manager.start(CountGroup.Main, mode=StartMode.RESET_STACK)
        await dialog_manager.done()

    @classmethod
    async def get_data(cls, dialog_manager: DialogManager, **kwargs):
        return {
            "compliments_count": cls._compliments_count,
        }

    @classmethod
    def create(cls):
        return Dialog(
            Window(
                Format("{compliments_count}"),
                state=CountGroup.Main,
                getter=cls.get_data,
            ),
            launch_mode=LaunchMode.ROOT,
        )

    @classmethod
    def register(cls, dp: Dispatcher, router: Router, **kwargs):
        router.message.register(cls.count_handler, Command("count"))

        dp.include_router(cls.create())
