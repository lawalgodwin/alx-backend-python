#!/usr/bin/env python3
"""Add the correct typings to the function below"""

from typing import Tuple, Union, List, Iterable, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A function that returns a list"""
    zoomed_in = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
