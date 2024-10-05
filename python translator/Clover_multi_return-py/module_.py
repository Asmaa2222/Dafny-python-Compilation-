import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
import _dafny as _dafny
import System_ as System_

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def MultipleReturns(x, y):
        more: int = int(0)
        less: int = int(0)
        more = (x) + (y)
        less = (x) - (y)
        return more, less

# Test the MultipleReturns function
if __name__ == "__main__":
    x = 10
    y = 5
    
    # Call the MultipleReturns function
    more, less = default__.MultipleReturns(x, y)
    
    # Print the results
    print(f"MultipleReturns({x}, {y}) -> more: {more}, less: {less}")
    
    # Testing other cases
    a, b = default__.MultipleReturns(7, 9)
    print(f"MultipleReturns(7, 9) -> more: {a}, less: {b}")  # Expect more: 16, less: -2

    a, b = default__.MultipleReturns(-3, -7)
    print(f"MultipleReturns(-3, -7) -> more: {a}, less: {b}")  # Expect more: -10, less: 4

    a, b = default__.MultipleReturns(0, 0)
    print(f"MultipleReturns(0, 0) -> more: {a}, less: {b}")  # Expect more: 0, less: 0
