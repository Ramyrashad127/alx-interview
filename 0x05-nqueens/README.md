# 0x05. N Queens

## Description
The **N Queens** problem is the challenge of placing $N$ non-attacking queens on an $N \times N$ chessboard. This project implements a backtracking algorithm in Python to compute and display all possible solutions for any integer $N \ge 4$.

## Requirements
- Interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code style: `pycodestyle` (version 2.8.*)
- Only `sys` module is allowed
- All files must be executable

## CLI Validation Rules
- Usage: `nqueens N`
- If user provides incorrect number of arguments, print `Usage: nqueens N` and exit status `1`.
- If `N` is not an integer, print `N must be a number` and exit status `1`.
- If `N < 4`, print `N must be at least 4` and exit status `1`.

## Tasks

| File | Description |
| :--- | :--- |
| `0-nqueens.py` | Complete backtracking solver that prints every valid board configuration, formatted as a list of `[row, col]` coordinates. |

## Usage & Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
