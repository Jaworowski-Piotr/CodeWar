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
    if 0 in board:
        return "Not finished yet", -1
    elif win_check(board, 1):
        return "Gracz X wygrał", 1
    elif win_check(board, 2):
        return "Gracz O wygrał", 2
    else:
        return "Nikt nie wygrał", 0


print(is_solved(board=[[0, 0, 1],
                       [0, 1, 2],
                       [2, 1, 0]]))