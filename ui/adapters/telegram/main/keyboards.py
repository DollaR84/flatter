from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from barsik.localisation import Localisation


async def get_menu_keyboard(lang: str, local: Localisation, is_panic: bool = False) -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    if is_panic:
        button_text = await local.fs("btn", "sos", lang)
        builder.button(text=button_text, request_location=True)
    else:
        button_text = await local.fs("btn", "want", lang)
        builder.button(text=button_text)

    builder.adjust(1)
    return builder.as_markup()
