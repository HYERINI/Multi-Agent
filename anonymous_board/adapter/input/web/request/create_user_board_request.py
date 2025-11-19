from pydantic import BaseModel

class CreateUserBoardRequest(BaseModel):
    author_id: int
    title: str
    content: str