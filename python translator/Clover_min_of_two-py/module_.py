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
    def Min(x, y):
        z: int = int(0)
        if (x) < (y):
            z = x
            return z
        elif True:
            z = y
            return z
        return z

if __name__ == "__main__":
    x = 10
    y = 5
    
    # Call the Min function
    result = default__.Min(x, y)
    
    # Print the result
    print(f"Min({x}, {y}) = {result}")
    
    # Testing other cases
    print(f"Min(7, 9) = {default__.Min(7, 9)}")  # Expect 7
    print(f"Min(-3, -7) = {default__.Min(-3, -7)}")  # Expect -7
    print(f"Min(0, 0) = {default__.Min(0, 0)}")  # Expect 0