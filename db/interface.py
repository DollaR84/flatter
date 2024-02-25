from config import Config

from barsik.db import BaseDB

from models import User

from .adapters import *

from .mapper import DataMapper


class DB(BaseDB):

    def __init__(self, cfg: Config, *names: list[str]):
        super().__init__(cfg, *names)
        self.mapper = DataMapper(self.adapter)

    async def update_panic_mode(self, user: User, is_panic: bool):
        return await self.mapper.update(user, is_panic=is_panic)

    async def update_location(self, user: User, location: str):
        return await self.mapper.update(user, location=location)
