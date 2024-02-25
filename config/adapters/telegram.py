from dataclasses import dataclass
import os

from barsik.config.adapters.telegram import TelegramAdapter, TelegramData as BaseTelegramData


@dataclass
class TelegramData(BaseTelegramData):
    receiver_chat_id: str = os.getenv("RECEIVER_CHAT_ID")


TelegramAdapter.data = TelegramData
