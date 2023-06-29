#!/usr/bin/python3
"""
Module for solving the prime game question.
"""


def isWinner(x, nums):
    """
    Function that checks for the winner.

    Args:
        x (int): The number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str or None
    """

    # Check for invalid inputs
    if not nums or x < 1:
        return None

    # Find the maximum number in the nums list
    max_num = max(nums)

    # Create a boolean list to mark prime numbers
    is_prime = [True for _ in range(max(max_num + 1, 2))]

    # Perform the prime sieve algorithm
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

    # Mark 0 and 1 as non-prime
    is_prime[0] = is_prime[1] = False

    # Calculate the cumulative count of prime numbers encountered
    prime_count = [0 for _ in range(len(is_prime))]
    count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    # Count the number of wins for Maria
    maria_wins = 0
    for num in nums:
        maria_wins += prime_count[num] % 2 == 1

    # Determine the winner based on the number of wins
    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
