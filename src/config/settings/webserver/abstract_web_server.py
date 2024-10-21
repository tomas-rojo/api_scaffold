from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, PositiveInt


class AbstractWebServer(ABC, BaseModel):
    host: str = "0.0.0.0"
    port: int = 5005
    debug: bool = True
    workers: PositiveInt = 4

    @abstractmethod
    def run(self, application: Any) -> None:
        raise NotImplementedError
