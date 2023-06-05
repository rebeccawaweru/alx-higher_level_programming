#!/usr/bin/python3
import sys

"""Solve the N-queens puzzle.
Atrributes:
    mat: the list of lists
    moves: contains solutions
"""


def init_mat(n):
    """Initialize `n`x`n`"""
    mat = []
    [mat.append([]) for j in range(n)]
    [row.append(' ') for j in range(n) for row in mat]
    return (mat)


def mat_copy(mat):
    """Return a copy of chessboard"""
    if isinstance(mat, list):
        return list(map(mat_copy, mat))
    return (mat)


def mat_move(mat):
    """Return list of lists with solution"""

    moves = []
    for x in range(len(mat)):
        for y in range(len(mat)):
            if mat[x][y] == "Q":
                moves.append([x, y])
                break
    return (moves)


def out(mat, row, col):
    """ spots on the chessbord
    Arguments:
    mat: the current chessboard (list)
    row: where queen was played last (integer)
    col: where queen was played last (integer)
    """
    for x in range(col + 1, len(mat)):
        mat[row][x] = "x"
    for x in range(col - 1, -1, -1):
        mat[row][x] = "x"
    for y in range(row + 1, len(mat)):
        mat[y][col] = "x"
    for y in range(row - 1, -1, -1):
        mat[y][col] = "x"
    x = col + 1
    for b in range(row + 1, len(mat)):
        if x >= len(mat):
            break
        mat[b][x] = "x"
        x += 1
    x = col - 1
    for b in range(row - 1, -1, -1):
        if x < 0:
            break
        mat[b][x]
        x -= 1
    x = col + 1
    for b in range(row - 1, -1, -1):
        if x >= len(mat):
            break
        mat[b][x] = "x"
        c += 1
    x = col - 1
    for b in range(row + 1, len(mat)):
        if x < 0:
            break
        mat[b][x] = "x"
        x -= 1


def solve(mat, row, queen, moves):
    """solve an N-queens puzzle
    Arguments:
    mat: the current chessboard
    row: the current row
    queen: the no of queens
    moves: solutions
    """
    if queen == len(mat):
        moves.append(mat_move(mat))
        return moves
    for x in range(len(mat)):
        if mat[row][x] == "":
            c_mat = mat_copy(mat)
            c_mat[row][x] = "Q"
            out(c_mat, row, x)
            moves = solve(c_mat, row + 1, queen + 1, moves)
    return (moves)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    mat = init_mat(int(sys.argv[1]))
    moves = solve(mat, 0, 0, [])
    for move in moves:
        print(move)
