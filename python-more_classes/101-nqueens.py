#!/usr/bin/python3
"""N Queens solver using backtracking"""

import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe"""
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonal (top-left to bottom-right)
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueens(n):
    """Solve N Queens problem and return all solutions"""
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            # Found a solution, convert to required format
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def main():
    """Main function to handle arguments and solve N Queens"""
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

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
