#!/usr/bin/env python3
"""A module that contains a type-annotated function sum_list which
takes a list input_list of floats as argument and returns their
sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats given"""
    sum = 0.0
    for f in input_list:
        sum = sum + f
    return sum
