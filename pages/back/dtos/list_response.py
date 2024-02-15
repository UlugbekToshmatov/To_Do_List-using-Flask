from dataclasses import dataclass
from datetime import datetime


@dataclass
class ListResponse:
    id: int
    name: str
    created_date: datetime
