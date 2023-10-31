#!/usr/bin/python3
import sys


def is_safe_to_play(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True


def s_nqueen(n):
    if n < 4:
        return []

    def solve(board, col):
        if col == n:
            result.append(board[:])
        else:
            for row in range(n):
                if is_safe_to_play(board, row, col):
                    board[col] = row
                    solve(board, col + 1)

    result = []
    board = [-1] * n
    solve(board, 0)
    return result


def printing_nqeen(solutions):
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = s_nqueen(n)
    printing_nqeen(solutions)
