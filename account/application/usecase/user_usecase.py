from typing import Optional, List
from account.application.port.user_repository_port import UserRepositoryPort
from account.domain.user import User

class UserUseCase:
    def __init__(self, user_repo: UserRepositoryPort):
        self.user_repo = user_repo

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repo.find_by_id(user_id)

    def list_users(self) -> List[User]:
        return self.user_repo.find_all()

    def update_user(self, user_id: int, name: str) -> Optional[User]:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            return None
        user.update_name(name)
        return self.user_repo.save(user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repo.delete(user_id)