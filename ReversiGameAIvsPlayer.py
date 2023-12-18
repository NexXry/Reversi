# from JoliReversi import Board // Ajout des numéros de colonnes en haut et des numéros de lignes à gauche
from Reversi import Board
from ReversiAI import ReversiAI


# Classe qui implémente le jeu AI VERS PLAYER
class ReversiGame:
    def __init__(self, color=Board._BLACK):
        self.board = Board(boardsize=10)
        self.ai = ReversiAI()
        self.current_player = "human"
        self.color = color

    def current_player_is_human(self):
        return self.current_player == "human"

    def switch_player(self):
        if self.current_player == "human":
            self.current_player = "ai"
        else:
            self.current_player = "human"

    def play_game(self):
        while not self.board.is_game_over():
            print(self.board)
            if self.current_player_is_human():
                move = self.get_human_move(self.color)
                self.board.push(move)
                self.switch_player()
            else:
                move = self.ai.find_best_move(self.board)
                self.board.push(move)
                self.switch_player()
        print(self.display_winner(self))

    def get_human_move(self, player):
        while True:
            move = input("Entrez votre coup (format ligne,colonne) ou '' pour passer : ")
            if move == '':
                return [player, -1, -1]
                print("Vous ne pouvez pas passer. Il y a des coups disponibles.")
            try:
                x, y = map(int, move.split(','))
                move = [player, x, y]
                legal_moves = self.board.legal_moves()
                for legal_move in legal_moves:
                    if legal_move[1] == x and legal_move[2] == y:
                        return move
                else:
                    print("Coup illégal. Réessayez.")
            except ValueError:
                print("Coup illégal. Réessayez.")

    def display_winner(self):
        nb_white, nb_black = self.board.get_nb_pieces()
        if self.color == Board._WHITE and nb_white > nb_black:
            print("Vous avez gagné avec", nb_white, "pièces contre", nb_black, "pour l'IA.")
        elif nb_black > nb_white:
            print("L'IA a gagné avec", nb_black, "pièces contre", nb_white, "pour vous.")
        else:
            print("La partie se termine par un match nul !")
