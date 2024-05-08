#!/usr/bin/python3
"""A method that determines if a given data set represents a valid
UTF-8 encoding."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data: A list of integers representing bytes of data.
    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    def is_continuation(byte):
        return byte & 0b11000000 == 0b10000000

    for byte in data:
        if byte < 0 or byte > 255:
            return False
        if byte <= 0x7F:
            continue
        if byte & 0b11100000 == 0b11000000:
            span = 1
        elif byte & 0b11110000 == 0b11100000:
            span = 2
        elif byte & 0b11111000 == 0b11110000:
            span = 3
        else:
            return False
        for i in range(1, span + 1):
            if not (i < len(data) and is_continuation(data[i])):
                return False
    return True
