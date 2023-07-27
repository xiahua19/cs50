"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                num_x += 1
            elif board[i][j] == O:
                num_o += 1
    
    if num_x > num_o:
        return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return list(possible_actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("invalid move")
    
    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(result_board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_positions = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(0,1), (1,1), (2,1)],
        [(0,0), (1,0), (2,0)],
        [(0,0), (1,1), (2,2)],
        [(2,0), (2,1), (2,2)],
        [(0,2), (1,2), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for win_position in win_positions:
        a, b, c = win_position
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] == X:
            return X
        elif board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] == O:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X, O] or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0  

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    possible_actions = actions(board)

    v = []

    if current_player == "X":
        for action in possible_actions:
            v.append(min_opt(result(board, action)))
        max_v = max(v)
        for idx, x in enumerate(v):
            if x == max_v:
                return possible_actions[idx]
    else:
        for action in possible_actions:
            v.append(max_opt(result(board, action)))
        min_v = min(v)
        for idx, x in enumerate(v):
            if x == min_v:
                return possible_actions[idx]

def max_opt(board):
    if terminal(board):
        return utility(board)

    possible_actions = actions(board)
    max_score = -2
    for action in possible_actions:
        max_score = max(max_score, min_opt(result(board, action)))
    return max_score

def min_opt(board):
    if terminal(board):
        return utility(board)

    possible_actions = actions(board)
    min_score = 2
    for action in possible_actions:
        min_score = min(min_score, max_opt(result(board, action)))
    return min_score