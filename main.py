import asyncio

from barsik.providers import BotProvider, CoreProvider

from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka

from providers import ConfigProvider, MainProvider, ServiceProvider


async def main():
    config = ConfigProvider()
    main = MainProvider(config.config, config.configurations)
    core = CoreProvider(config.config)
    bot = BotProvider(config.config, main.ui)
    service = ServiceProvider(config.config)

    container = make_async_container(config, core, bot, main, service)
    setup_dishka(container=container, router=bot.dp)

    try:
        await bot.dp.start_polling(bot.bot)
    finally:
        await container.close()
        await bot.bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
