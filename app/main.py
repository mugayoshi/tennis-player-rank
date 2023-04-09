from typing import Union

from fastapi import FastAPI
from app.players.schemas import AtpPlayer
from app.players.services import get_atp_players

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/players/atp")
def get_players() -> list[AtpPlayer]:
    return get_atp_players()
    