from dataclasses import dataclass

from barsik.models import User as BaseUser


@dataclass
class User(BaseUser):
    is_panic: bool = False
    location: str | None = None
