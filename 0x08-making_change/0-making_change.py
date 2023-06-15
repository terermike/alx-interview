#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        coin_multiplier = total // coin
        coin_count += coin_multiplier
        total -= (coin_multiplier * coin)
    if total != 0:
        return -1
    return coin_count
