"""Utility functies."""


def greet(name: str) -> str:
    """Begroet een gebruiker."""
    return f"Welkom bij {name}!"


def reverse_string(s: str) -> str:
    """Draai een string om."""
    return s[::-1]


def fibonacci(n: int) -> list[int]:
    """Genereer eerste n Fibonacci getallen."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib
