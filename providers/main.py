from config import Config

from db import DB

from dishka import Provider, Scope, provide

from ui import UI


class MainProvider(Provider):

    def __init__(self, config: Config, configurations: list[str]):
        super().__init__()

        self.db: DB = DB(config, *configurations)
        self.ui: UI = UI(config, *configurations)

    @provide(scope=Scope.APP)
    def get_db(self) -> DB:
        return self.db

    @provide(scope=Scope.APP)
    def get_ui(self) -> UI:
        return self.ui
