from .handlers import CommandHandlers, MessageHandlers

from .about import AboutDialog

from .count import CountDialog


class Main:

    @classmethod
    def register(cls, **kwargs):
        AboutDialog.register(**kwargs)
        CountDialog.register(**kwargs)

        CommandHandlers.register(**kwargs)
        MessageHandlers.register(**kwargs)
