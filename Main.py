# Choix du mode de jeu IA VS IA ou IA VS JOUEUR
from Reversi import Board
from ReversiGameAIvsPlayer import ReversiGame

from ReversiGameAivsAi import ReversiGame as ReversiGameIA

choice = input("Choisissez le mode de jeu : \n 1 - IA VS JOUEUR \n 2 - IA VS IA  \n")
choiceColor = input("Choisissez la couleur de l'IA ou du Joueur : \n 1 - NOIR \n 2 - BLANC \n")


def game():
    gameStart = True
    while gameStart:
        if choice == "1":
            if choiceColor == "1":
                game = ReversiGame(color=Board._BLACK)
            else:
                game = ReversiGame(color=Board._WHITE)
            game.play_game()
            gameStart = False
        elif choice == "2":
            if choiceColor == "1":
                game = ReversiGameIA(color=Board._BLACK)
            else:
                game = ReversiGameIA(color=Board._WHITE)
            game.play_game()
            gameStart = False
        else:
            print("Choix invalide, veuillez réessayer.")


# Démarrage du jeu
game()
