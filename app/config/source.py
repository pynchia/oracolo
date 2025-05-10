from pydantic import BaseModel


class SourceSettings(BaseModel):
    # The credentials used by the API Proxy service
    # to authenticate on the DRS API
    api_key: str
    api_url: str
