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
    def CalDiv():
        x: int = int(0)
        y: int = int(0)
        rhs0_ = 0
        rhs1_ = 191
        x = rhs0_
        y = rhs1_
        while (7) <= (y):
            x = (x) + (1)
            y = (191) - ((7) * (x))
        return x, y

if __name__ == "__main__":
    # Call the CalDiv function
    quotient, remainder = default__.CalDiv()
    
    # Print the results
    print(f"CalDiv() -> quotient: {quotient}, remainder: {remainder}")
