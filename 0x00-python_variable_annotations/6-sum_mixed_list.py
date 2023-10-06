#!/usr/bin/env python3
"""A module that contains a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns their
sum as a float.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the given list of numbers as float"""
    sum = 0.0
    for num in mxd_lst:
        sum = float(sum + num)
    return sum
