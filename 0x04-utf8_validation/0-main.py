#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
print(validUTF8([0x41]))          # True, 'A'
print(validUTF8([0xC2, 0xA9]))    # True, ©
print(validUTF8([0xE2, 0x82, 0xAC]))  # True, €
print(validUTF8([0xF0, 0x9F, 0x8D, 0x95]))  # True, 🍕
print(validUTF8([0x80]))          # False, invalid single byte
print(validUTF8([0xC2, 0x28]))    # False, invalid continuation byte
print(validUTF8([0xE2, 0x28, 0xAC]))  # False, invalid continuation byte
print(validUTF8([0xF0, 0x28, 0x8C, 0xBC]))  # False, invalid continuation byte
