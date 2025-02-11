#!/usr/bin/env python3
import math
from typing import List

def fibonacci(n: int) -> List[int]:
    """
    Generate a Fibonacci sequence with n elements.
    
    Parameters:
        n (int): The number of elements in the Fibonacci sequence.
    
    Returns:
        List[int]: A list containing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def factorial(n: int) -> int:
    """
    Compute the factorial of n using recursion.
    
    Parameters:
        n (int): A non-negative integer.
        
    Returns:
        int: The factorial of n.
        
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

class Calculator:
    """
    A simple calculator class to demonstrate LSP features with methods,
    type annotations, and exception handling.
    """
    def __init__(self, initial_value: float = 0.0) -> None:
        self.value = initial_value

    def add(self, amount: float) -> None:
        self.value += amount

    def subtract(self, amount: float) -> None:
        self.value -= amount

    def multiply(self, factor: float) -> None:
        self.value *= factor

    def divide(self, divisor: float) -> None:
        if divisor == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= divisor

    def get_value(self) -> float:
        return self.value

def main() -> None:
    # Test the Fibonacci function
    print("Fibonacci sequence (10 numbers):")
    fib_seq = fibonacci(10)
    print(fib_seq)

    # Test the factorial function
    try:
        print("\nFactorial of 5:", factorial(5))
    except ValueError as e:
        print("Error computing factorial:", e)

    # Test the Calculator class
    print("\nCalculator operations:")
    calc = Calculator(10)
    calc.add(5)
    calc.subtract(3)
    calc.multiply(2)
    try:
        calc.divide(0)  # This should trigger an error.
    except ValueError as e:
        print("Caught error during division:", e)
    calc.divide(4)
    print("Final calculator value:", calc.get_value())

if __name__ == "__main__":
    main()