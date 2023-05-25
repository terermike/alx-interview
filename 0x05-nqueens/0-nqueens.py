#!/usr/bin/python3
import sys


def initialize_board(size):
    """Initialize an `size`x`size` sized chessboard with empty spaces."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board


def deepcopy_board(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Return the list of queen positions in a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
    return solution


def mark_attacked_spots(board, row, col):
    """Mark spots on the chessboard where queens can no longer be placed."""
    size = len(board)

    for c in range(col + 1, size):
        board[row][c] = "x"  # Mark forward spots

    for c in range(col - 1, -1, -1):
        board[row][c] = "x"  # Mark backward spots

    for r in range(row + 1, size):
        board[r][col] = "x"  # Mark spots below

    for r in range(row - 1, -1, -1):
        board[r][col] = "x"  # Mark spots above

    r, c = row + 1, col + 1
    while r < size and c < size:
        board[r][c] = "x"  # Mark spots diagonally down to the right
        r += 1
        c += 1

    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"  # Mark spots diagonally up to the left
        r -= 1
        c -= 1

    r, c = row - 1, col + 1
    while r >= 0 and c < size:
        board[r][c] = "x"  # Mark spots diagonally up to the right
        r -= 1
        c += 1

    r, c = row + 1, col - 1
    while r < size and c >= 0:
        board[r][c] = "x"  # Mark spots diagonally down to the left
        r += 1
        c -= 1


def solve_nqueens(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle."""
    size = len(board)

    if queens == size:
        solutions.append(get_solution(board))
        return

    for col in range(size):
        if board[row][col] == " ":
            new_board = deepcopy_board(board)
            new_board[row][col] = "Q"
            mark_attacked_spots(new_board, row, col)
            solve_nqueens(new_board, row + 1, queens + 1, solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(N)
    solutions = []

