# core.py

from uuid import uuid4, UUID
from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    id: UUID = field(default_factory=uuid4)