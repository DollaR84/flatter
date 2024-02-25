import logging
import random

from config import Config


class Compliments:

    def __init__(self, config: Config):
        self.file_path: str = config.services.compliments_file_path

        self.data: list[str] = []

        self.load(self.file_path)

        random.seed()
        random.shuffle(self.data)

    def load(self, file_path: str):
        try:
            with open(file_path, "r", encoding="utf-8") as db_file:
                data = db_file.read()
                self.data = list(data.split("***"))
        except IOError as error:
            logging.error(error, exc_info=True)
            raise IOError("Error: open compliments file...") from error

    def get(self) -> str:
        return random.choice(self.data)
