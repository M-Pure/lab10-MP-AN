#https://github.com/M-Pure/lab10-MP-AN.git
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/M-Pure/lab10-MP-AN.git
# Partner 1: Maddex Pure
# Partner 2: Alfred Navarro

import math

def square_root(a):
    try:
        sqrt = math.sqrt(a)
        return sqrt
    except Exception as e:
        raise ValueError("Error: Negative Square Root")

def hypotenuse(a, b):
    try:
        if a == 0 or b == 0:
            raise ValueError("Error: Invalid Side Length")
        return math.hypot(a, b)
    except Exception as e:
        print(str(e))

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator is zero")
    return b / a

def logarithm(a, b):
    if b <= 0:
        raise ValueError("Undefined logarithm")
    if a <= 0 or a == 1:
        raise ValueError("Invalid logarithm base")
    return math.log(b, a)

def exp(a, b):
    return a ** b



