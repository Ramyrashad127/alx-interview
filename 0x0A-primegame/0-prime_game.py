#!/usr/bin/python3
"""Prime Game module"""


def isWinner(x, nums):
    """Prime Game function"""
    Maria = 0
    Ben = 0
    prime = [0, 0]
    for i in range(2, 10005):
        prime.append(1)

    for i in range(2, 10001):
        if prime[i] == 1:
            for j in range(i + i, 10001, i):
                prime[j] = 0

    for i in range(1, 10001):
        prime[i] += prime[i-1]

    for n in nums:
        if prime[n] % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria < Ben:
        return "Ben"
    if Maria > Ben:
        return "Maria"
    return None
