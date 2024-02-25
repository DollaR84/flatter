from barsik.ui import BaseUI

from config import Config

from .adapters import *


class UI(BaseUI):

    def __init__(self, cfg: Config, *names: list[str]):
        super().__init__(cfg, *names)
