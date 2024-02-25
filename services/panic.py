from db import DB

from models import User


class Panic:

    async def change_status(self, db: DB, user: User) -> bool:
        new_panic_status = not user.is_panic
        await db.update_panic_mode(user, is_panic=new_panic_status)
        return new_panic_status

    async def save_location(self, db: DB, user: User, location: str):
        await db.update_location(user, location=location)
