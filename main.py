#!/usr/bin/env python3
"""Test Python project voor claude-dev VM."""

from calculator import Calculator
from utils import greet


def main():
    print(greet("Claude-dev"))
    
    calc = Calculator()
    
    print(f"\n10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    
    print(f"\nIs 17 prime? {calc.is_prime(17)}")
    print(f"Is 18 prime? {calc.is_prime(18)}")


if __name__ == "__main__":
    main()
