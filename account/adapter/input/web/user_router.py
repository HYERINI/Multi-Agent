from typing import List

from fastapi import APIRouter, HTTPException, Depends

from account.adapter.input.web.request.update_user_request import UpdateUserRequest
from account.adapter.input.web.response.user_response import UserResponse
from account.application.usecase.user_usecase import UserUseCase
from account.infrastructure.repository.user_repository_impl import UserRepositoryImㄴ

user_router = APIRouter()

def get_user_usecase() -> UserUseCase:
    return UserUseCase(UserRepositoryImpl())

@user_router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, usecase: UserUseCase = Depends(get_user_usecase)):
    user = usecase.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        created_at=user.created_at,
    )

@user_router.get("/users", response_model=List[UserResponse])
def list_users(usecase: UserUseCase = Depends(get_user_usecase)):
    users = usecase.list_users()
    return [
        UserResponse(
            id=u.id,
            email=u.email,
            name=u.name,
            created_at=u.created_at,
        )
        for u in users
    ]

@user_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    request: UpdateUserRequest,
    usecase: UserUseCase = Depends(get_user_usecase),
):
    user = usecase.update_user(user_id, request.name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        created_at=user.created_at,
    )

@user_router.delete("/users/{user_id}")
def delete_user(user_id: int, usecase: UserUseCase = Depends(get_user_usecase)):
    success = usecase.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Deleted successfully"}
