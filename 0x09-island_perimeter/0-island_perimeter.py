#!/usr/bin/python3
"""island_perimeter"""


def island_perimeter(grid):
    """island_perimeter"""
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if(j-1 >= 0 and grid[i][j-1] == 0):
                    cnt += 1
                if (j+1 < len(grid[i]) and grid[i][j+1] == 0):
                    cnt += 1
                if (i-1 >= 0 and grid[i-1][j] == 0):
                    cnt += 1
                if (i+1 < len(grid) and grid[i+1][j] == 0):
                    cnt += 1
                if (i == 0):
                    cnt += 1
                if (i == len(grid)-1):
                    cnt += 1
                if (j == 0):
                    cnt += 1
                if (j == len(grid[i])-1):
                    cnt += 1
    return cnt
