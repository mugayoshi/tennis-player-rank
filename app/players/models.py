from pydantic import BaseModel

class AtpPlayerRecord (BaseModel):
    name: str
    rank: int
    country: str
    thumbnail_url: str