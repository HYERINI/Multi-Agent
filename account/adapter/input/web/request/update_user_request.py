from pydantic import BaseModel

class UpdateUserRequest(BaseModel):
    name: str