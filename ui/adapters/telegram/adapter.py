from barsik.ui.base import BaseUIAdapter

from .main import Main


class TelegramAdapter(BaseUIAdapter):

    @classmethod
    def register(cls, **kwargs):
        Main.register(**kwargs)
