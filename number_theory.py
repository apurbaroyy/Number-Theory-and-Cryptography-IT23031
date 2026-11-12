"""Introductory number-theory functions for the workshop."""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def euler_totient(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)
