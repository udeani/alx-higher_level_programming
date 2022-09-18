#!/usr/bin/python3

"""Defines an integer add function."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.
    Floats are changed to integer
    Raises a typeerror if neither a or b is an integer"""
    
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
