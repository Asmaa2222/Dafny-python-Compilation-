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
    def Abs(x):
        y: int = int(0)
        if (x) < (0):
            y = (0) - (x)
            return y
        elif True:
            y = x
            return y
        return y

if __name__ == '__main__':
    test_values = [-10, 0, 15, -7, 20]
    # Applying the original Abs function to each test value
    results_original = {val: default__.Abs(val) for val in test_values}
    print(results_original)