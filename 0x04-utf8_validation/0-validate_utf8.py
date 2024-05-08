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
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]
        if byte & 0b10000000 == 0:
            # single byte character
            i += 1
        elif byte & 0b11100000 == 0b11000000:
            # two byte character
            if i + 1 >= len(data) or not is_continuation(data[i + 1]):
                return False
            i += 2
        elif byte & 0b11110000 == 0b11100000:
            # three byte character
            if i + 2 >= len(data) or \
               not is_continuation(data[i + 1]) or \
               not is_continuation(data[i + 2]):
                return False
            i += 3
        elif byte & 0b11111000 == 0b11110000:
            # four byte character
            if i + 3 >= len(data) or \
               not is_continuation(data[i + 1]) or \
               not is_continuation(data[i + 2]) or \
               not is_continuation(data[i + 3]):
                return False
            i += 4
        else:
            return False
    return True
