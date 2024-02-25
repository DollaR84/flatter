from barsik.config import BaseConfig

from .adapters import *


class Config(BaseConfig):

    def __init__(self, *names: list[str], **kwargs):
        super().__init__(*names, **kwargs)
