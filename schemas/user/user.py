from barsik import schemas


class User(schemas.User):
    is_panic: bool = False
    location: str | None = None
