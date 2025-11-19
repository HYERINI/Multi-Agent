from typing import List, Optional

from anonymous_board.application.port.anonymous_board_repository_port import AnonymousBoardRepositoryPort
from anonymous_board.domain.anonymous_board import AnonymousBoard


class AnonymousBoardUseCase:
    def __init__(self, board_repo: AnonymousBoardRepositoryPort):
        self.board_repo = board_repo

    # 1) 익명 글 작성
    def create_anonymous_board(self, title: str, content: str) -> AnonymousBoard:
        board = AnonymousBoard(title=title, content=content, author_id=None)
        return self.board_repo.save(board)

    # 2) 특정 유저가 작성한 글
    def create_board_by_user(self, author_id: int, title: str, content: str) -> AnonymousBoard:
        board = AnonymousBoard(title=title, content=content, author_id=author_id)
        return self.board_repo.save(board)

    # 3) 특정 게시글 조회 (board_id)
    def get_board(self, board_id: int) -> Optional[AnonymousBoard]:
        return self.board_repo.get_by_id(board_id)

    # 4) 전체 게시글 조회
    def list_boards(self) -> List[AnonymousBoard]:
        return self.board_repo.list_all()

    # 5) 게시글 수정
    def update_board(self, board_id: int, title: str, content: str) -> Optional[AnonymousBoard]:
        board = self.board_repo.get_by_id(board_id)
        if not board:
            return None
        board.update(title, content)
        return self.board_repo.save(board)

    # 6) 게시글 삭제
    def delete_board(self, board_id: int) -> None:
        self.board_repo.delete(board_id)
