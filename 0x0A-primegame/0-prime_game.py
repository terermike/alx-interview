#!/usr/bin/python3


def isWinner(x, nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        maria_turn = True

        while primes:
            if maria_turn:
                player = "Maria"
            else:
                player = "Ben"

            max_prime = max(primes)
            primes.remove(max_prime)

            for num in range(max_prime, n + 1, max_prime):
                if num in primes:
                    primes.remove(num)

            maria_turn = not maria_turn

        wins[player] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
