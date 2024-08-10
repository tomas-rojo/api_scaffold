from pydantic import BaseModel


class WebSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 5005
    debug: bool = False
