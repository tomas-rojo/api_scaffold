import uuid
from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class User:
    email: str
    is_active: bool = False
    id: uuid.UUID = field(default_factory=uuid.uuid4)
