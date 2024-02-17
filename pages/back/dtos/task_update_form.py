from dataclasses import dataclass
from datetime import datetime


@dataclass
class TaskUpdateForm:
    name: str
    notes: str
    priority: str
    due_date: datetime
    completed: bool
