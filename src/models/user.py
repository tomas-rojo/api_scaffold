from dataclasses import dataclass


@dataclass(kw_only=True, slots=True, frozen=True)
class User:
    id: str
    email: str
    is_active: bool = False
