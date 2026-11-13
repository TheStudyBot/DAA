n = 4
board = [[0] * n for i in range(n)]

# Place first queen
board[0][1] = 1

# Check safe position
def is_safe(row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row + 1, col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Solve using backtracking
def solve(col):

    if col >= n:
        return True

    for row in range(n):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(col + 1):
                return True

            board[row][col] = 0

    return False

if solve(1):
    print("N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution")