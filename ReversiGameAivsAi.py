from Reversi import Board
from ReversiAI import ReversiAI


class ReversiGame:
    def __init__(self, color=Board._BLACK):
        self.board = Board(boardsize=10)
        self.ai_black = ReversiAI()
        self.ai_white = ReversiAI()
        self.current_player = color

    def switch_player(self):
        self.current_player = self.board._flip(self.current_player)

    def play_game(self):
        while not self.board.is_game_over():
            print(self.board)
            move = None
            if self.current_player == Board._BLACK:
                move = self.ai_black.find_best_move(self.board)
            else:
                move = self.ai_white.find_best_move(self.board)

            if move:
                self.board.push(move)
            self.switch_player()
        print(self.board)
        self.display_winner()

    def display_winner(self):
        nb_white, nb_black = self.board.get_nb_pieces()
        if nb_white > nb_black:
            print("Le vainqueur est l'IA BLANCHE avec", nb_white, "pièces contre", nb_black, "pour l'IA NOIRE.")
        elif nb_black > nb_white:
            print("Le vainqueur est l'IA NOIRE avec", nb_black, "pièces contre", nb_white, "pour l'IA BLANCHE.")
        else:
            print("La partie se termine par un match nul !")
