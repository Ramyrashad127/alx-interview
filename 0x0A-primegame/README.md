# 0x0A. Prime Game

## Description
This project solves the **Prime Game** problem using game theory and prime number sieving.

Maria and Ben play $x$ rounds of a game with a set of consecutive integers from $1$ to $n$. In each round:
1. They take turns choosing a prime number from the set.
2. The chosen prime and all of its multiples are removed from the set.
3. The player who cannot make a move loses the game.
4. Maria always plays first, and both players play optimally.

## Optimization Strategy
- Use the **Sieve of Eratosthenes** to precompute prime numbers up to the maximum $n$ in the rounds.
- Build a prefix sum array of prime counts to evaluate round winners in $O(1)$ time per round.

## Requirements
- Interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code style: `pycodestyle` (version 2.8.*)
- Do not import external packages

## Tasks

| File | Description | Complexity |
| :--- | :--- | :--- |
| `0-prime_game.py` | Function `def isWinner(x, nums):` where `x` is the number of rounds and `nums` is an array of `n`. Returns the name of the player that won the most rounds, or `None` if tied. | Time: $O(M \log(\log M) + x)$, Space: $O(M)$ |

## Usage & Example

```bash
$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

$ ./main_0.py
Winner: Ben
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
