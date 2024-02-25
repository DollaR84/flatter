from barsik.providers import types

from config import Config

from dishka import Provider, Scope, provide


class ConfigProvider(Provider):

    def __init__(self):
        super().__init__()

        self.configurations = [
            types.Main.CORE.value,
            types.Main.LOCALISATION.value,
            types.Main.GEO.value,
            types.Main.SERVICES.value,
            types.DB.SQLITE.value,
            types.Storage.REDIS.value,
            types.GUI.TELEGRAM.value
        ]

        self.config: Config = Config(*self.configurations)

    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return self.config
