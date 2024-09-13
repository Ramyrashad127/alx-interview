#!/usr/bin/python3


"""import modules"""


def validUTF8(data):
    """function to check data"""
    def is_continuation_byte(byte):
        """start with 10xxxxxx"""
        return 128 <= byte <= 191

    i = 0
    n = len(data)
    while i < n:
        byte = data[i]

        if byte < 128:
            num_bytes = 1
        elif 192 <= byte <= 223:
            num_bytes = 2
        elif 224 <= byte <= 239:
            num_bytes = 3
        elif 240 <= byte <= 247:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > n:
            return False

        for j in range(1, num_bytes):
            if not is_continuation_byte(data[i + j]):
                return False
        i += num_bytes

    return True
