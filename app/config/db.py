from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    url: str
