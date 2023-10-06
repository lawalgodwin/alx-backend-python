#!/usr/bin/env python3
"""Annotate a given function"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Count the number of elements in a list"""
    return [(i, len(i)) for i in lst]
