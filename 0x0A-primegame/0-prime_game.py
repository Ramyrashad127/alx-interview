#!/usr/bin/python3
"""Prime Game module ALX"""


def isWinner(x, nums):
    """Prime Game function ALX"""
    Maria = 0
    Ben = 0
    limit = max(nums)
    prime = [0] * (limit + 1)

    for i in range(2, limit + 1):
        prime[i] = 1

    for i in range(2, int(limit ** 0.5) + 1):
        if prime[i] == 1:
            for j in range(i * i, limit + 1, i):
                prime[j] = 0

    for i in range(1, limit + 1):
        prime[i] += prime[i - 1]

    for n in range(x):
        if prime[n] % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria < Ben:
        return "Ben"
    if Maria > Ben:
        return "Maria"
    return None
