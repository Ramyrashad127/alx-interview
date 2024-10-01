#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """get total from coins"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    check = 0
    temp = 0
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
