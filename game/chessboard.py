import chess
from chess import Board

from .configs import BOARD_SCORES, END_SCORES

NAME_TO_SQUARE = dict(zip(chess.SQUARE_NAMES, chess.SQUARES))


def square_name(move):
    return move.uci()[:2]


def turn_side(board):
    side = "White" if board.turn else "Black"
    return side


def game_over(board: Board, claim_draw: bool = False) -> bool:
    if board.is_game_over(claim_draw=claim_draw):
        return True
    return False


def check_win(board: Board, player: bool) -> bool:
    if board.is_checkmate() and board.turn == (not player):
        return True
    return False


def check_tie(board: Board, claim_draw: bool = False) -> bool:
    tie = board.is_stalemate() or board.is_fivefold_repetition() or board.is_insufficient_material()
    if claim_draw:
        tie = tie or board.can_claim_draw()
    if tie:
        return True
    return False
