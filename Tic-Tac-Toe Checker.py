def win_check(tablica, znak):
    return ((tablica[2][0] == znak and tablica[2][1] == znak and tablica[2][2] == znak) or  # across the top
            (tablica[1][0] == znak and tablica[1][1] == znak and tablica[1][2] == znak) or  # across the middle
            (tablica[0][0] == znak and tablica[0][1] == znak and tablica[0][2] == znak) or  # across the bottom
            (tablica[2][0] == znak and tablica[1][0] == znak and tablica[0][0] == znak) or  # down the middle
            (tablica[2][1] == znak and tablica[1][1] == znak and tablica[0][1] == znak) or  # down the middle
            (tablica[2][2] == znak and tablica[1][2] == znak and tablica[0][2] == znak) or  # down the right side
            (tablica[2][0] == znak and tablica[1][1] == znak and tablica[0][2] == znak) or  # diagonal
            (tablica[2][2] == znak and tablica[1][1] == znak and tablica[0][0] == znak))  # diagonal

def is_solved(board):

    if win_check(board, 1):
        return 1
    elif win_check(board, 2):
        return 2
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return -1
                    break
        return 0


print(is_solved(board=[[0, 0, 1],
                       [0, 1, 2],
                       [2, 1, 0]]))

#Inne ciekawe rozwiązanie
# import itertools
#
# def isSolved(board):
#     b = list(itertools.chain(*board))
#     for p, q, r in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
#         if b[p] == b[q] == b[r] != 0: return b[p]
#     return 0 if sum(b) == 13 else -1