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
    countX = 0
    countO = 0
    for i in board:
        for j in i:
            if j == "X":
                countX += 1
            elif j == "O":
                countO += 1
    if countX > countO:
        return "O"
    else:
        return "X"
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return (0,0)
    res = []
    i = 0
    j = 0
    for row in board:
        for col in row:
            if col == EMPTY:
                res.append((i, j))
            j += 1
        j = 0
        i += 1

    return res
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        return board
    res = copy.deepcopy(board)
    turn = player(res)
    i = action[0]
    j = action[1]

    if turn == X:
        res[i][j] = 'X'
    elif turn == O:
        res[i][j] = 'O'

    return res
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    numRow = len(board[0])
    numCol = len(board)
    #check for row
    for i in range(0, numRow):
        row = set([board[i][0], board[i][1], board[i][2]])
        if len(row) == 1 and board[i][0] != None:
            return board[i][0]

    #check for col
    for i in range(0, numCol):
        col = set([board[0][i], board[1][i], board[2][i]])
        if len(col) == 1 and board[0][i] != None:
            return board[0][i]

    #check for diag
    diag1 = set([board[0][0], board[1][1], board[2][2]])
    diag2 = set([board[0][2], board[1][1], board[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and board[1][1] != None:
        return board[1][1]

    return None
    raise NotImplementedError

def isBoardFull(board):
    for row in board:
        if EMPTY in row:
            return False

    return True

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if isBoardFull(board):
        return True
    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0
    raise NotImplementedError

def minValue(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        res = result(board, action)
        v = min(v, maxValue(res))
    return v
def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        res = result(board, action)
        v = max(v, minValue(res))
    return v

# return the score
def alphaBetaPruning(alpha, beta, player, level, board):
    if terminal(board) or level == 0:
        return utility(board), None
    optimalAct = (0,0)
    if player == X:
        for action in actions(board):
            score, _ = alphaBetaPruning(alpha, beta, O, level-1, result(board, action))
            if score > alpha:
                alpha = score
                optimalAct = action
            if alpha >= beta:
                break
        return alpha, optimalAct
    elif player == O:
        for action in actions(board):
            score, _ = alphaBetaPruning(alpha, beta, X, level-1, result(board, action))
            if score < beta:
                beta = score
                optimalAct = action
            if alpha >= beta:
                break
        return beta, optimalAct
        



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # X is max player, O is min player
    p = player(board)
<<<<<<< HEAD
    # if p == X:
    #     u = -2
    #     optimalAction = None
    #     for action in actions(board):
    #         if minValue(board) > u:
    #             optimalAction = action
    #     return optimalAction
    # elif p == O:
    #     u = 2
    #     optimalAction = None
    #     for action in actions(board):
    #         if maxValue(board) < u:
    #             optimalAction = action
    #     return optimalAction
    _ , res = alphaBetaPruning(-2, 2, p, 9, board)
    return res
=======
    if p == X:
        u = -2
        optimalAction = None
        for action in actions(board):
            newU = minValue(result(board, action))
            if newU > u:
                optimalAction = action
                u = newU
        return optimalAction
    elif p == O:
        u = 2
        optimalAction = None
        for action in actions(board):
            newU = maxValue(result(board, action))
            if newU < u:
                optimalAction = action
                u = newU
        return optimalAction

>>>>>>> d8e82277dd0a918840f37db382f0ba63e14c54e0
    raise NotImplementedError
