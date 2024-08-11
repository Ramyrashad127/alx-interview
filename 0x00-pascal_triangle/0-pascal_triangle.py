#!/usr/bin/python3
"""
no modules
"""


def pascal_triangle(n):
    """ new function"""
    if n <= 0:
        return []

    li = [[1]]

    for i in range(1, n):
        prev = [1]
        for j in range(1, i):
            prev.append(li[i-1][j-1] + li[i-1][j])
        prev.append(1)
        li.append(prev)

    return li
