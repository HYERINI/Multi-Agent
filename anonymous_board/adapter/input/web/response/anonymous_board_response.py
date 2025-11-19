from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class AnonymousBoardResponse(BaseModel):
    id: int
    author_id: Optional[int]
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
