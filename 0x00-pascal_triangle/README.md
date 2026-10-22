# 0x00. Pascal's Triangle

## Description
This project implements an algorithmic function in Python that generates **Pascal's Triangle** for an arbitrary integer `n`.

Pascal's triangle is a triangular array of binomial coefficients. In the triangle, each number is the sum of the two directly above it.

## Learning Objectives
- Understanding triangular number patterns and binomial coefficients.
- Generating multidimensional lists in Python.
- Optimizing list construction and boundary handling.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code style: `pycodestyle` (version 2.8.*)
- All files must be executable

## Tasks

| File | Description | Complexity |
| :--- | :--- | :--- |
| `0-pascal_triangle.py` | Function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`. Returns an empty list if `n <= 0`. | Time: $O(n^2)$, Space: $O(n^2)$ |

## Usage & Example

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
