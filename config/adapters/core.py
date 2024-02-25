from dataclasses import dataclass

from barsik.config.adapters.core import CoreAdapter


@dataclass
class CoreData:
    app_name: str = "flatter"


CoreAdapter.data = CoreData
