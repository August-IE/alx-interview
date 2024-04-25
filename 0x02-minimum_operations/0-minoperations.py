#!/usr/bin/python3
'''In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given
a number n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int) or n <= 0:
        return 0

    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0 or (n - done) % done == 0:
            clipboard = done
            ops_count += 2
        else:
            ops_count += 1
        done += clipboard

    return ops_count
