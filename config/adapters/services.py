from dataclasses import dataclass

from barsik.config.adapters.services import ServicesAdapter


@dataclass
class ServicesData:
    compliments_file_path: str = "services/compliments.db"


ServicesAdapter.data = ServicesData
