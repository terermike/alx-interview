#!/usr/bin/python3


def isWinner(x, nums):
    """Function that checks for the winner"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    is_prime = [True] * (max(max_num + 1, 2))

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    is_prime[0] = is_prime[1] = False

    prime_count = [0] * len(is_prime)
    prime_sum = 0

    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_sum += 1
        prime_count[i] = prime_sum

    maria_wins = 0

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == len(nums):
        return None
    elif maria_wins + 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
