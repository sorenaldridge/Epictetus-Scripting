from datetime import datetime
from pony.orm import *


db = Database()


class NetworkSlice(db.Entity):
    id = PrimaryKey(int, auto=True)
    up = Required(int)
    down = Required(int)
    timestamp = Required(datetime)


class Torrent(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    completed = Required(datetime)
    size = Optional(int)


db.bind(provider="sqlite", filename="network.db", create_db=True)
db.generate_mapping(create_tables=True)
