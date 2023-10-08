#!/usr/bin/env python3
"""Add the correct typings to the function below"""

from typing import Union, List


def zoom_array(lst: List[int], factor: Union[int, float] = 2) -> List[int]:
    """A function that returns a list"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)