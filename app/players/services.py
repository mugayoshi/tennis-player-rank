from app.players.schemas import AtpPlayer
from app.database import get_db
from app.players.models import AtpPlayerRecord
from typing import List

def get_atp_players() -> list[AtpPlayer]:
    db = get_db();
    rows = db['atp'].find()
    result: List[AtpPlayer] = []
    for item in rows:
        model = AtpPlayerRecord(**item)
        schema = AtpPlayer(name=model.name, country=model.country, rank=model.rank, thumbnail=model.thumbnail_url)
        result.append(schema)
    return result