import itertools
from chess import Board, Move

from .generic_player import GenericPlayer
from ..chessboard import turn_side


class HumanPlayer(GenericPlayer):
    def __init__(self, player: bool):
        super().__init__(player, "human")

    def _get_move(self, board: Board) -> str:
        uci = input(f"({turn_side(board)}) Your turn! Choose move (in uci): ")

        # check legal uci move
        try:
            Move.from_uci(uci)
        except ValueError:
            uci = None
        return uci

    def _print_moves(self, moves):
        iters = [iter(moves)] * 4
        iters = itertools.zip_longest(*iters)

        for group in iters:
            print(" | ".join(move for move in group if move is not None))

    def move(self, board: Board) -> str:
        assert board.turn == self.player, "Not your turn to move!"

        legal_moves = [move.uci() for move in board.legal_moves]
        move = self._get_move(board)

        while move is None:
            print("Invalid uci move! Try again.", )
            move = self._get_move(board)

        while move not in legal_moves:
            print("Not a legal move! Avaliable moves:\n")
            self._print_moves(legal_moves)
            move = self._get_move(board)

        return move
