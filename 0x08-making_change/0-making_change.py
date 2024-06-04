#!/usr/bin/python3
"""Change comes from within .
"""


def makeChange(coins, total):
    """Given a pile of coins of different values in order to determine the
    fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    i = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while i > 0:
        if coin_idx >= n:
            return -1
        if i - sorted_coins[coin_idx] >= 0:
            i -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
