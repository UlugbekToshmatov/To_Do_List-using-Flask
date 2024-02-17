from datetime import datetime
from dataclasses import dataclass


@dataclass
class TaskResponse:
    id: int
    name: str
    notes: str
    priority: str
    due_date: datetime
    completed: bool
    created_date: datetime
    list_id: int
