# 0x04. UTF-8 Validation

## Description
This project focuses on bitwise manipulation and binary validation by implementing an algorithm to verify whether a given dataset represents a valid **UTF-8 encoding**.

## UTF-8 Encoding Rules
1. A 1-byte character starts with `0` followed by 7 bits (`0xxxxxxx`).
2. A 2-byte character starts with `110` followed by 5 bits (`110xxxxx`), and the continuation byte begins with `10` (`10xxxxxx`).
3. A 3-byte character starts with `1110` (`1110xxxx`), followed by two continuation bytes starting with `10` (`10xxxxxx`).
4. A 4-byte character starts with `11110` (`11110xxx`), followed by three continuation bytes starting with `10` (`10xxxxxx`).

## Requirements
- Interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code style: `pycodestyle` (version 2.8.*)
- All files must be executable

## Tasks

| File | Description | Complexity |
| :--- | :--- | :--- |
| `0-validate_utf8.py` | Function `def validUTF8(data):` that returns `True` if `data` is a valid UTF-8 encoding, else `False`. Each integer represents 1 byte of data (only the 8 least significant bits are examined). | Time: $O(N)$, Space: $O(1)$ |

## Usage & Example

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""
validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 254]
print(validUTF8(data))

$ ./0-main.py
True
True
False
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
