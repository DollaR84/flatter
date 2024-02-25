from typing import Annotated

from aiogram import Router, types
from aiogram.filters.command import Command, CommandStart

from barsik.aiogram.functions import get_user, get_name
from barsik.localisation import Localisation

from dishka.integrations.aiogram import Depends, inject

from db import DB

from models import User

from services.panic import Panic

from ..keyboards import get_menu_keyboard


class CommandHandlers:

    @classmethod
    @inject
    async def start_handler(
            cls, message: types.Message,
            db: Annotated[DB, Depends()],
            local: Annotated[Localisation, Depends()],
    ):
        user = User.from_schema(get_user(message))
        name = get_name(user)
        user = await db.get_and_update_user(user)

        message_text = await local.fs("phrases", "start", user.lang, name=name)
        menu_keyboard = await get_menu_keyboard(user.lang, local, user.is_panic)

        await message.answer(message_text, reply_markup=menu_keyboard, parse_mode="HTML")

    @classmethod
    @inject
    async def panic_handler(
            cls, message: types.Message,
            panic: Annotated[Panic, Depends()],
            db: Annotated[DB, Depends()],
            local: Annotated[Localisation, Depends()],
    ):
        user = User.from_schema(get_user(message))
        user = await db.get_and_update_user(user)

        is_panic = await panic.change_status(db, user)

        panic_mode = "on" if is_panic else "off"
        message_text = await local.fs("phrases", f"panic_{panic_mode}", user.lang)

        keyboard = await get_menu_keyboard(user.lang, local, is_panic)
        await message.answer(message_text, reply_markup=keyboard, parse_mode="HTML")

    @classmethod
    def register(cls, router: Router, **kwargs):
        router.message.register(cls.start_handler, CommandStart())
        router.message.register(cls.panic_handler, Command("panic"))
