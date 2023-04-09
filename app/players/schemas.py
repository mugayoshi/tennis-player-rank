from typing  import List

from pydantic import BaseModel

class AtpPlayer(BaseModel):
    name: str
    rank: int
    country: str
    thumbnail: str


    

    

