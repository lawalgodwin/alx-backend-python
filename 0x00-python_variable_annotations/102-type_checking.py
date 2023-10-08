#!/usr/bin/python3
"""Add the correct typings to the function below"""

from typing import Union, List


def zoom_array(lst: List[int], factor: int = 2) -> List:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
