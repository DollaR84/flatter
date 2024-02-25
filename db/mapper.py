from barsik.db.base import BaseDBAdapter
from barsik.db.mapper import BaseDataMapper

from db import models as db_models

import models


class DataMapper(BaseDataMapper):

    def __init__(self, adapter: BaseDBAdapter):
        super().__init__(adapter, db_models, models)
