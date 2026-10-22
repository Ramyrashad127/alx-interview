# 0x09. Island Perimeter

## Description
This project implements an algorithm to compute the perimeter of an island defined in a 2D grid of integers:
- `0` represents water.
- `1` represents land.
- Grid cells are connected horizontally and vertically (not diagonally).
- The grid is completely surrounded by water, and there is exactly one island without internal lakes.

## Algorithm
Iterate through the grid. For every land cell (`1`):
1. Start with 4 potential perimeter edges.
2. If the upper neighbor is land, subtract 1 (or 2 for mutual edge).
3. If the left neighbor is land, subtract 1 (or 2 for mutual edge).
4. Total accumulated perimeter is returned with $O(\text{rows} \times \text{cols})$ time complexity.

## Requirements
- Interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code style: `pycodestyle` (version 2.8.*)
- Do not import any modules

## Tasks

| File | Description | Complexity |
| :--- | :--- | :--- |
| `0-island_perimeter.py` | Function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`. | Time: $O(R \times C)$, Space: $O(1)$ |

## Usage & Example

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

$ ./0-main.py
12
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
