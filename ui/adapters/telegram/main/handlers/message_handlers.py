from aiogram import Bot, F, types
from aiogram import Router

from barsik.aiogram.functions import get_user, get_name
from barsik.geo import GeoOSM
from barsik.localisation import Localisation

from config import Config

from dishka.integrations.aiogram import FromDishka

from db import DB

from models import User

from services.compliments import Compliments
from services.panic import Panic


class MessageHandlers:

    @classmethod
    async def location_handler(
            cls, message: types.Message,
            geo: FromDishka[GeoOSM],
            panic: FromDishka[Panic],
            db: FromDishka[DB],
            local: FromDishka[Localisation],
            bot: FromDishka[Bot],
            cfg: FromDishka[Config],
    ):
        user = User.from_schema(get_user(message))
        name = get_name(user)
        user = await db.get_user(user)

        latitude_str = await local.fs("phrases", "latitude", user.lang)
        longitude_str = await local.fs("phrases", "longitude", user.lang)

        coordinates = message.location
        coords_str = ", ".join([
            f"{latitude_str}: {coordinates['latitude']}",
            f"{longitude_str}: {coordinates['longitude']}",
        ])
        await message.delete()

        location = await geo.get_location(coordinates)
        await panic.save_location(db, user, location)

        message_text = await local.fs(
            "phrases", "panic_msg", user.lang,
            userName=name, userId=user.chat_id,
            coordinates=coords_str, location=location,
        )

        await bot.send_message(chat_id=cfg.telegram.receiver_chat_id, text=message_text)
        await message.answer(await local.fs("phrases", "panic_answer", user.lang), parse_mode="HTML")

    @classmethod
    async def menu_handler(
            cls, message: types.Message,
            compliments: FromDishka[Compliments],
            db: FromDishka[DB],
            local: FromDishka[Localisation],
    ):
        user = User.from_schema(get_user(message))
        user = await db.get_user(user)

        if await local.fs("btn", "want", user.lang) == message.text:
            await message.delete()

            message_text = compliments.get()
            await message.answer(message_text, parse_mode="HTML")

    @classmethod
    def register(cls, router: Router, **kwargs):
        router.message.register(cls.location_handler, F.location)
        router.message.register(cls.menu_handler, F.text)
