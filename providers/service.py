from config import Config

from dishka import Provider, Scope, provide

from services.compliments import Compliments
from services.panic import Panic


class ServiceProvider(Provider):

    def __init__(self, config: Config):
        super().__init__()

        self.compliments: Compliments = Compliments(config)
        self.panic: Panic = Panic()

    @provide(scope=Scope.APP)
    def get_compliment(self) -> Compliments:
        return self.compliments

    @provide(scope=Scope.APP)
    def get_panic(self) -> Panic:
        return self.panic
