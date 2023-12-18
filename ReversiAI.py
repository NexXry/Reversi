from Reversi import Board


# Classe qui implémente l'IA
class ReversiAI:
    def __init__(self, color=Board._BLACK, depth=3):
        self.color = color
        self.depth = depth

    # Fonction minimax avec élagage alpha-beta
    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves():
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves():
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    # Fonction qui réalise le compte des pions du plateau
    def count_pawns(self, board):
        player_pawns, opponent_pawns = board.get_nb_pieces()
        return player_pawns, opponent_pawns

    # Fonction qui réalise le compte des pions du plateau dans les coins en fonction de la couleur du joueur
    def count_corners(self, board):
        player_corners = 0
        opponent_corners = 0
        corners = [(0, 0), (0, 9), (9, 0), (9, 9)]  # Coordonnées des coins pour un plateau de taille 10

        for x, y in corners:
            if board._board[x][y] == board._BLACK:
                player_corners += 1
            elif board._board[x][y] == board._WHITE:
                opponent_corners += 1

        return player_corners, opponent_corners

    # Fonction qui évalue la stabilité (Note sur la difficulté à prendre le pion) des pions du plateau
    def evaluate_stability(self, board):
        player_stability = 0
        opponent_stability = 0

        for i in range(board._boardsize):
            for j in range(board._boardsize):
                if i == 0 or i == board._boardsize - 1 or j == 0 or j == board._boardsize - 1:
                    # Pièce sur un bord ou dans un coin
                    if board._board[i][j] == board._BLACK:
                        player_stability += 1
                    elif board._board[i][j] == board._WHITE:
                        opponent_stability += 1

        return player_stability, opponent_stability

    # Fonction qui évalue la mobilité (Note sur le nombre de coups possibles) des pions du plateau
    def evaluate_mobility(self, board):
        player_mobility = 0
        opponent_mobility = 0
        for i in range(board._boardsize):
            for j in range(board._boardsize):
                if board._board[i][j] == board._BLACK:
                    player_mobility += board.testAndBuild_ValidMove(board._BLACK, i, j) if 1 else 0
                elif board._board[i][j] == board._WHITE:
                    opponent_mobility += board.testAndBuild_ValidMove(board._BLACK, i, j) if 1 else 0
        return player_mobility, opponent_mobility

    # Fonction qui évalue le plateau en fonction de différents facteurs (nombre de pions, stabilité, mobilité) ce sonts les heuristiques
    def evaluate_board(self, board):
        player_pawns, opponent_pawns = self.count_pawns(board)
        pawn_difference = player_pawns - opponent_pawns

        player_corners, opponent_corners = self.count_corners(board)
        corner_control = player_corners - opponent_corners

        player_stability, opponent_stability = self.evaluate_stability(board)
        stability = player_stability - opponent_stability

        player_mobility, opponent_mobility = self.evaluate_mobility(board)
        mobility = player_mobility - opponent_mobility

        # Ponderation des différents facteurs
        score = 50 * pawn_difference + 100 * corner_control + 70 * stability + 50 * mobility
        return score

    # Fonction qui trouve le meilleur coup possible en fonction de l'évaluation du plateau grave à la fonction minimax et l'élagage alpha-beta
    def find_best_move(self, board):
        best_move = None
        best_value = float('-inf')
        for move in board.legal_moves():
            board.push(move)
            move_value = self.minimax(board, self.depth, float('-inf'), float('inf'), False)
            board.pop()
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move
