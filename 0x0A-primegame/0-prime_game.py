#!/usr/bin/python3
"""Prime game by two players."""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the numbers in each round.

    Returns:
        str: The name of the player with the most wins ('Maria' or 'Ben').
        None: If there is no winner.
    """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes up to the maximum number in nums
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Calculate the cumulative number of primes up to each index
    for num in nums:
        primes_count = sum(primes[0:num])
        if primes_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
