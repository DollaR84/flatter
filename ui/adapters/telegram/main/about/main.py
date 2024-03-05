from typing import Annotated

from aiogram import Dispatcher, Router, types
from aiogram.filters.command import Command

from aiogram_dialog import Dialog, DialogManager, LaunchMode, StartMode, Window

from barsik.aiogram.functions import get_user
from barsik.aiogram.dialog.widgets.text import FormatLocalisation

from dishka.integrations.aiogram import FromDishka, inject

from db import DB

from models import User

from .states import AboutGroup


class AboutDialog:

    @classmethod
    @inject
    async def about_handler(
            cls, message: types.Message,
            dialog_manager: DialogManager,
            db: Annotated[DB, FromDishka()],
    ):
        user = User.from_schema(get_user(message))
        user = await db.get_and_update_user(user)
        data = {"lang": user.lang}

        await dialog_manager.start(AboutGroup.Main, data=data, mode=StartMode.RESET_STACK)
        await dialog_manager.done()

    @classmethod
    def create(cls):
        return Dialog(
            Window(
                FormatLocalisation("author", "about"),
                state=AboutGroup.Main,
            ),
            launch_mode=LaunchMode.ROOT,
        )

    @classmethod
    def register(cls, dp: Dispatcher, router: Router, **kwargs):
        router.message.register(cls.about_handler, Command("about"))

        dp.include_router(cls.create())
