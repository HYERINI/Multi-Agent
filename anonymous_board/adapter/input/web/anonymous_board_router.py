from typing import List

from fastapi import APIRouter, HTTPException, Depends

from anonymous_board.adapter.input.web.request.create_anonymous_board_request import CreateAnonymousBoardRequest
from anonymous_board.adapter.input.web.request.create_user_board_request import CreateUserBoardRequest
from anonymous_board.adapter.input.web.request.update_board_request import UpdateBoardRequest
from anonymous_board.adapter.input.web.response.anonymous_board_response import AnonymousBoardResponse
from anonymous_board.application.usecase.anonymous_board_usecase import AnonymousBoardUseCase
from anonymous_board.infrastructure.repository.anonymous_board_repository_impl import AnonymousBoardRepositoryImpl

anonymous_board_router = APIRouter()

def get_board_usecase() -> AnonymousBoardUseCase:
    return AnonymousBoardUseCase(AnonymousBoardRepositoryImpl())

# 1) 게시글 익명 작성
@anonymous_board_router.post("/create/anonymous", response_model=AnonymousBoardResponse)
def create_anonymous_board(
    request: CreateAnonymousBoardRequest,
    usecase: AnonymousBoardUseCase = Depends(get_board_usecase),
):
    board = usecase.create_anonymous_board(request.title, request.content)
    return AnonymousBoardResponse(
        id=board.id,
        author_id=board.author_id,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

# 2) 게시글 유저 작성
@anonymous_board_router.post("/create/user", response_model=AnonymousBoardResponse)
def create_user_board(
    request: CreateUserBoardRequest,
    usecase: AnonymousBoardUseCase = Depends(get_board_usecase),
):
    board = usecase.create_board_by_user(request.author_id, request.title, request.content)
    return AnonymousBoardResponse(
        id=board.id,
        author_id=board.author_id,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

@anonymous_board_router.get("/list", response_model=List[AnonymousBoardResponse])
def list_boards(usecase: AnonymousBoardUseCase = Depends(get_board_usecase)):
    boards = usecase.list_boards()
    return [
        AnonymousBoardResponse(
            id=b.id,
            author_id=b.author_id,
            title=b.title,
            content=b.content,
            created_at=b.created_at,
            updated_at=b.updated_at,
        ) for b in boards
    ]

# 단건 조회
@anonymous_board_router.get("/read/{board_id}", response_model=AnonymousBoardResponse)
def get_board(board_id: int, usecase: AnonymousBoardUseCase = Depends(get_board_usecase)):
    board = usecase.get_board(board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return AnonymousBoardResponse(
        id=board.id,
        author_id=board.author_id,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

# 게시글 수정
@anonymous_board_router.put("/update/{board_id}", response_model=AnonymousBoardResponse)
def update_board(
    board_id: int,
    request: UpdateBoardRequest,
    usecase: AnonymousBoardUseCase = Depends(get_board_usecase),
):
    board = usecase.update_board(board_id, request.title, request.content)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return AnonymousBoardResponse(
        id=board.id,
        author_id=board.author_id,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

# 게시글 삭제
@anonymous_board_router.delete("/delete/{board_id}")
def delete_board(board_id: int, usecase: AnonymousBoardUseCase = Depends(get_board_usecase)):
    success = usecase.delete_board(board_id)
    if not success:
        raise HTTPException(status_code=404, detail="Board not found")
    return {"message": "Deleted successfully"}