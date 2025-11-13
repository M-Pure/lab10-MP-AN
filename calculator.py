"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Error: Negative Square Root")
        return math.sqrt(a)
    except Exception as e:
        print(str(e))

def hypotenuse(a, b):
    try:
        if a == 0 or b == 0:
            raise ValueError("Error: Invalid Side Length")
        return math.hypot(a, b)
    except Exception as e:
        print(str(e))

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def log(a, b):
    if b <= 0:
        raise ValueError("Undefined logarithm")
    if a <= 0 or a == 1:
        raise ValueError("Invalid logarithm base")
    return math.log(b, a)

def exp(a, b):
    return a ** b



