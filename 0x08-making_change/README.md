# 0x08. Making Change

## Description
This project addresses the classic **Coin Change Problem**: Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total amount.

## Strategy & Optimization
- If `total <= 0`, return `0`.
- When coin denominations cannot compose the total, return `-1`.
- A greedy approach works for canonical coin systems, while Dynamic Programming (or greedy with fallback) solves arbitrary denomination arrays efficiently.

## Requirements
- Interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code style: `pycodestyle` (version 2.8.*)
- Runtime efficiency is strictly evaluated

## Tasks

| File | Description | Complexity |
| :--- | :--- | :--- |
| `0-making_change.py` | Function `def makeChange(coins, total):` that returns the minimum coins needed. | Time: $O(n \log n + \text{total})$, Space: $O(1)$ or $O(\text{total})$ |

## Usage & Example

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))

$ ./0-main.py
7
-1
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
