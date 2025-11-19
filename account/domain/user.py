from typing import Optional
from datetime import datetime

class User:
    def __init__(self, email: str, name: str):
        self.id: Optional[int] = None
        self.email = email
        self.name = name
        self.created_at: datetime = datetime.utcnow()

    def update_name(self, name: str):
        self.name = name