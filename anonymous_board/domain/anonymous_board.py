from typing import Optional
from datetime import datetime

class AnonymousBoard:
    def __init__(self, title: str, content: str, author_id: Optional[int] = None):
        self.id: Optional[int] = None
        self.author_id: Optional[int] = author_id #None이면 완전 익명
        self.title = title
        self.content = content
        self.created_at: datetime = datetime.utcnow()
        self.updated_at: datetime = datetime.utcnow()

    def update(self, title: str, content: str):
        self.title = title
        self.content = content
        self.updated_at = datetime.utcnow()
