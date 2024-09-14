#!/usr/bin/python3


"""import modules"""
import sys


ans = []


def construct(row, n):
    """Backtracking to place queens"""
    if row == n:
        print(ans)
        return

    for col in range(n):
        is_safe = True
        for a in ans:
            if a[1] == col or abs(row - a[0]) == abs(col - a[1]):
                is_safe = False
                break
        if is_safe:
            ans.append((row, col))
            construct(row + 1, n)
            ans.pop()


def nqueen(n):
    """return list of integers for positions of n queens on n*n chessboard"""
    try:
        n = int(n)
    except Exception:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    construct(0, n)


if __name__ == "__main__":
    n = sys.argv[1]
    nqueen(n)
