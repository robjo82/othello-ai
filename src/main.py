import copy
import time


# Initialisation du plateau de jeu
def init_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    board[3][3], board[4][4] = 'W', 'W'
    board[3][4], board[4][3] = 'B', 'B'
    return board


# Affichage du plateau de jeu
def display_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, end=' ')
        for cell in row:
            print(cell, end=' ')
        print()


# Vérification de la validité d'un mouvement
def is_valid_move(board, x, y, player):
    # Détermine la couleur de l'adversaire
    opponent = 'W' if player == 'B' else 'B'

    # Vérifie si la case est déjà occupée
    if board[x][y] != ' ':
        return False, []  # Le coup n'est pas valide, pas de cellules retournées

    # Liste des huit directions possibles (voisins)
    directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]

    # Liste pour stocker les cellules à retourner
    flipped_cells = []

    # Parcours de chaque direction possible
    for dx, dy in directions:
        # Initialise une liste pour les cellules à retourner dans cette direction
        temp_flips = []
        # Déplacement initial à partir de la case de départ (x, y)
        nx, ny = x + dx, y + dy

        # Tant que les coordonnées sont à l'intérieur du plateau
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board[nx][ny] == opponent:
                # Ajoute les coordonnées de l'adversaire à la liste temporaire
                temp_flips.append((nx, ny))
            elif board[nx][ny] == player:
                if temp_flips:
                    # S'il y a des cellules adverses entre les cellules du joueur actuel,
                    # ajoute-les à la liste des cellules à retourner
                    flipped_cells.extend(temp_flips)
                break
            else:
                break  # La case est vide, donc le coup n'est pas valide
            # Met à jour les coordonnées pour passer à la case suivante dans la direction
            nx += dx
            ny += dy

    # Le coup est valide s'il y a des cellules à retourner
    return len(flipped_cells) > 0, flipped_cells


# Appliquer un mouvement sur le plateau
def make_move(board, x, y, player):
    is_valid, flipped_cells = is_valid_move(board, x, y, player)
    if is_valid:
        board[x][y] = player
        for fx, fy in flipped_cells:
            board[fx][fy] = player
    return is_valid


# Fonction d'évaluation simple
def evaluate_board(board, player):
    player_score = sum(cell == player for row in board for cell in row)
    opponent_score = sum(cell != ' ' and cell != player for row in board for cell in row)
    return player_score - opponent_score


# Mémoire des états déjà traités pour éviter les calculs redondants
memo = {}


def has_valid_move(board, player):
    taille_grille = len(board)

    for row in range(taille_grille):
        for col in range(taille_grille):
            if is_valid_move(board, row, col, player)[0]:
                return True

    return False


# Algorithme Min-Max avec time-out et mémoire
# def minmax_with_memory(board, depth, maximizing, player, timeout):
#     if time.time() > timeout:
#         return None, None

#     board_str = ''.join(''.join(row) for row in board) + player
#     if board_str in memo:
#         return memo[board_str]

#     if depth == 0:
#         score = evaluate_board(board, player)
#         memo[board_str] = score, None
#         return score, None

#     opponent = 'W' if player == 'B' else 'B'
#     best_move = None

#     if maximizing:
#         max_eval = float('-inf')
#         for x in range(8):
#             for y in range(8):
#                 new_board = copy.deepcopy(board)
#                 if make_move(new_board, x, y, player):
#                     eval_value, _ = minmax_with_memory(new_board, depth - 1, False, player, timeout)
#                     if eval_value is None:  # Timeout occurred
#                         return None, None
#                     if eval_value > max_eval:
#                         max_eval = eval_value
#                         best_move = (x, y)
#         memo[board_str] = max_eval, best_move
#         return max_eval, best_move
#     else:
#         min_eval = float('inf')
#         for x in range(8):
#             for y in range(8):
#                 new_board = copy.deepcopy(board)
#                 if make_move(new_board, x, y, opponent):
#                     eval_value, _ = minmax_with_memory(new_board, depth - 1, True, player, timeout)
#                     if eval_value is None:  # Timeout occurred
#                         return None, None
#                     if eval_value < min_eval:
#                         min_eval = eval_value
#                         best_move = (x, y)
#         memo[board_str] = min_eval, best_move
#         return min_eval, best_move

# def minmax_with_memory(board, depth, maximizing, player, timeout):
#     # Vérifie si le temps est écoulé (timeout) et renvoie un résultat vide si c'est le cas
#     if time.time() > timeout:
#         return None, None  # Timeout occurred

#     # Convertit le plateau de jeu en une chaîne pour stockage dans la mémoire (hash)
#     board_str = ''.join(''.join(row) for row in board) + player
#     # Si la configuration du plateau est déjà en mémoire, renvoie le résultat mémorisé
#     if board_str in memo:
#         return memo[board_str]

#     # Cas de base : si la profondeur d'exploration est de zéro, renvoie l'évaluation du plateau actuel
#     if depth == 0:
#         score = evaluate_board(board, player)
#         # Stocke le résultat en mémoire pour éviter de le recalculer
#         memo[board_str] = score, None
#         return score, None

#     # Détermine l'opposant du joueur actuel
#     opponent = 'W' if player == 'B' else 'B'
#     best_move = None
#     possible_moves = []  # Liste des mouvements possibles

#     # Si on maximise, c'est le tour du joueur actuel
#     if maximizing:
#         max_eval = float('-inf')
#         for x in range(8):
#             for y in range(8):
#                 new_board = copy.deepcopy(board)
#                 if make_move(new_board, x, y, player):
#                     # Appelle récursivement la fonction pour évaluer le mouvement
#                     eval_value, _ = minmax_with_memory(new_board, depth - 1, False, player, timeout)
#                     if eval_value is None:  # Si un timeout s'est produit, ajoute la position à la liste
#                         possible_moves.append((x, y))
#                     elif eval_value > max_eval:
#                         max_eval = eval_value
#                         best_move = (x, y)
#         # Si aucun meilleur mouvement n'a été trouvé, joue la première position possible
#         if best_move is None and possible_moves:
#             best_move = possible_moves[0]
#             # Évalue le plateau actuel pour stockage en mémoire
#             max_eval = evaluate_board(board, player)
#         # Stocke le résultat en mémoire
#         memo[board_str] = max_eval, best_move
#         return max_eval, best_move
#     # Si on minimise, c'est le tour de l'opposant
#     else:
#         min_eval = float('inf')
#         for x in range(8):
#             for y in range(8):
#                 new_board = copy.deepcopy(board)
#                 if make_move(new_board, x, y, opponent):
#                     # Appelle récursivement la fonction pour évaluer le mouvement
#                     eval_value, _ = minmax_with_memory(new_board, depth - 1, True, player, timeout)
#                     if eval_value is None:  # Si un timeout s'est produit, ajoute la position à la liste
#                         possible_moves.append((x, y))
#                     elif eval_value < min_eval:
#                         min_eval = eval_value
#                         best_move = (x, y)
#         # Si aucun meilleur mouvement n'a été trouvé, joue la première position possible
#         if best_move is None and possible_moves:
#             best_move = possible_moves[0]
#             # Évalue le plateau actuel pour stockage en mémoire
#             min_eval = evaluate_board(board, player)
#         # Stocke le résultat en mémoire
#         memo[board_str] = min_eval, best_move
#         return min_eval, best_move

MAX_SCORE = 1000000  # Choisissez une valeur appropriée pour MAX_SCORE


def minmax_with_memory(board, depth, maximizing, player, timeout, possible_moves):
    if depth == 0:
        return evaluate_board(board, player), None

    if time.time() >= timeout:
        if not possible_moves:
            return evaluate_board(board, player), (-1, -1)

        best_move = possible_moves[0]
        return evaluate_board(board, player), best_move

    board_str = ''.join(''.join(row) for row in board) + player

    if board_str in memo:
        return memo[board_str]

    opponent = 'W' if player == 'B' else 'B'
    best_move = None

    if maximizing:
        max_eval = -MAX_SCORE
        for move in possible_moves:
            x, y = move
            new_board = copy.deepcopy(board)
            if make_move(new_board, x, y, player):
                eval_value, _ = minmax_with_memory(new_board, depth - 1, False, player, timeout, possible_moves)
                if eval_value is None:
                    possible_moves.append((x, y))
                elif eval_value > max_eval:
                    max_eval = eval_value
                    best_move = (x, y)
        if best_move is None:
            best_move = possible_moves[0]
            max_eval = evaluate_board(board, player)
        memo[board_str] = max_eval, best_move
        return max_eval, best_move
    else:
        min_eval = MAX_SCORE
        for move in possible_moves:
            x, y = move
            new_board = copy.deepcopy(board)
            if make_move(new_board, x, y, opponent):
                eval_value, _ = minmax_with_memory(new_board, depth - 1, True, player, timeout, possible_moves)
                if eval_value is None:
                    possible_moves.append((x, y))
                elif eval_value < min_eval:
                    min_eval = eval_value
                    best_move = (x, y)
        if best_move is None:
            best_move = possible_moves[0]
            min_eval = evaluate_board(board, player)
        memo[board_str] = min_eval, best_move
        return min_eval, best_move


# Fonction pour récupérer le mouvement du joueur humain
def get_human_move(board, player):
    while True:
        try:
            x, y = map(int, input(f"Enter the coordinates where you want to place your '{player}' (row col): ").split())
            is_valid, _ = is_valid_move(board, x, y, player)
            if is_valid:
                return x, y
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")


def positions_jouables(board, player):
    positions = []
    for x in range(8):
        for y in range(8):
            if is_valid_move(board, x, y, player)[0]:
                positions.append((x, y))
    return positions


# Fonction principale pour jouer au jeu
def play_game():
    board = init_board()
    player_turn = 'W'

    while True:
        display_board(board)

        if player_turn == 'W':
            print("Human's turn:")
            x, y = get_human_move(board, 'W')
        else:
            print("AI's turn:")
            timeout = time.time() + 2  # 2 secondes de time-out pour l'IA
            _, (x, y) = minmax_with_memory(board, 3, True, 'B', timeout)
            if x is None and y is None:
                print("AI timeout. Human wins!")
                break

        make_move(board, x, y, player_turn)

        # Vérification de la fin du jeu
        if all(cell != ' ' for row in board for cell in row):
            w_score = sum(cell == 'W' for row in board for cell in row)
            b_score = sum(cell == 'B' for row in board for cell in row)
            print(f"Final scores - W: {w_score}, B: {b_score}")
            if w_score > b_score:
                print("Human wins!")
            elif b_score > w_score:
                print("AI wins!")
            else:
                print("It's a tie!")
            break

        player_turn = 'B' if player_turn == 'W' else 'W'


# Fonction principale pour jouer au jeu IA contre IA
def play_game_ai_vs_ai():
    board = init_board()
    player_turn = 'W'

    while True:
        display_board(board)
        print(f"{player_turn}'s turn:")
        timeout = time.time() + 2  # 2 secondes de time-out pour l'IA
        _, (x, y) = minmax_with_memory(board, 3, player_turn == 'W', player_turn, timeout)
        if x is None and y is None:
            print(f"{player_turn} timeout. Game over!")
            break

        make_move(board, x, y, player_turn)

        # Pause pour faciliter l'analyse
        time.sleep(1)

        # Vérification de la fin du jeu
        if all(cell != ' ' for row in board for cell in row):
            w_score = sum(cell == 'W' for row in board for cell in row)
            b_score = sum(cell == 'B' for row in board for cell in row)
            print(f"Final scores - W: {w_score}, B: {b_score}")
            if w_score > b_score:
                print("W wins!")
            elif b_score > w_score:
                print("B wins!")
            else:
                print("It's a tie!")
            break

        player_turn = 'B' if player_turn == 'W' else 'W'

# Jouer au jeu
# if __name__ == '__main__':
#     mode = input("Choose game mode (human or ai): ")
#     if mode == 'human':
#         play_game()
#     elif mode == 'ai':
#         play_game_ai_vs_ai()
#     else:
#         print("Invalid mode. Exiting.")
#         sys.exit(1)
