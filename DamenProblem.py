def vertical_move(board, amount=1, start=(0, 0), up=True):
    result = start
    if up:
        if start[0] - 1 - amount >= 0:
            result = (start[0] - amount, start[1])
    else:
        if start[0] + 1 + amount < len(board):
            result = (start[0] + amount)
    return result


def horizontal_move(board, amount=1, start=(0, 0), left=True):
    result = start
    if left:
        if start[1] - 1 - amount >= 0:
            result = (start[0] - amount, start[1])
    else:
        if [start[1]] + 1 + amount < len(board):
            result = (start[0] + amount)
    return result


def try_all_directions():
    pass


def solve_board(size=4):
    board = [list(0 for j in range(size)) for _ in range(size)]
    if size < 3:
        return None
    start_point = (size - 1, 0)
    board[size - 1][0] = 1
    for i in range(size):
        try:
            board[10320] = 1
        except:
            print("Error occured")


solve_board()
