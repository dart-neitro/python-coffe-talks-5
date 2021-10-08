# core.py
from uuid import uuid4, UUID
from dataclasses import dataclass, field


def get_default_user_id() -> UUID:
    return uuid4()


@dataclass
class User:
    name: str
    id: UUID = field(default_factory=get_default_user_id)