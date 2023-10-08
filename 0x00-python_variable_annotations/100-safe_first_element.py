#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from typing import Any, Union, Sequence, Optional


def safe_first_element(lst: Optional[Sequence[Any]]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
