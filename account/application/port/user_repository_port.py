from typing import Protocol, Optional, List
from account.domain.user import User

class UserRepositoryPort(Protocol):
    def save(self, user: User) -> User:
        ...

    def find_by_id(self, user_id: int) -> Optional[User]:
        ...

    def find_all(self) -> List[User]:
        ...

    def delete(self, user_id: int) -> bool:
        ...