def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

def solve(board):
    find = findEmpty(board)
    if not find:
        return True

    else:
        line, column = find

    for i in range(1,10):
        if valid(board, i, (line, column)):
            board[line][column] = i

            if solve(board):
                return True

            board[line][column] = 0

    return False


def valid(board, num, position):
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False

    return True