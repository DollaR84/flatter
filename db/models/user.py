from barsik.db.models.base import Base
from barsik.db.models.user import BaseUser
from barsik.db.mixins import BaseDBModel

import sqlalchemy as sa
import sqlalchemy.orm as so


class User(BaseUser, BaseDBModel, Base):

    is_panic: so.Mapped[bool] = so.mapped_column(default=False)
    location: so.Mapped[str | None] = so.mapped_column(nullable=True)

