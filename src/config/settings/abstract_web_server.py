from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, PositiveInt

class AbstractWebServer(ABC, BaseModel):
    host: str = "127.0.0.1"
    port: int = 5006
    debug: bool = True
    workers: PositiveInt = 4

    @abstractmethod
    def run(self, application: Any) -> None:
        raise NotImplementedError


