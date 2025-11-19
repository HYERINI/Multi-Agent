from typing import Optional, List
from datetime import datetime
from account.application.port.user_repository_port import UserRepositoryPort
from account.domain.user import User

class UserRepositoryImpl(UserRepositoryPort):
    def __init__(self):
        # 간단한 메모리 저장소
        self._users = {}
        self._id_counter = 1

    def save(self, user: User) -> User:
        # 신규 생성
        if user.id is None:
            user.id = self._id_counter
            user.created_at = datetime.utcnow()
            self._users[user.id] = user
            self._id_counter += 1
            return user

        # 기존 업데이트
        self._users[user.id] = user
        return user

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

    def find_all(self) -> List[User]:
        return list(self._users.values())

    def delete(self, user_id: int) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False
