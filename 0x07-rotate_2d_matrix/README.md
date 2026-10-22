# 0x07. Rotate 2D Matrix

## Description
This project implements an algorithm to rotate an $n \times n$ 2D matrix by **90 degrees clockwise** completely **in-place** without allocating a second matrix.

## Algorithmic Approach
1. **Transpose the matrix**: Swap elements across the main diagonal: `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`.
2. **Reverse each row**: Invert each row horizontally: `row.reverse()` or two-pointer swap.
3. Resulting time complexity is $O(n^2)$ and auxiliary space complexity is $O(1)$.

## Requirements
- Interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code style: `pycodestyle` (version 2.8.*)
- Do not import any external modules

## Tasks

| File | Description | Complexity |
| :--- | :--- | :--- |
| `0-rotate_2d_matrix.py` | Function `def rotate_2d_matrix(matrix):` that edits the matrix in-place. | Time: $O(n^2)$, Space: $O(1)$ |

## Usage & Example

```bash
$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

$ ./main_0.py
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
