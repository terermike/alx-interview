#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the fewest number of coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
