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
    def Sum(N):
        s: int = int(0)
        d_0_n_: int
        d_0_n_ = 0
        s = 0
        while (d_0_n_) != (N):
            d_0_n_ = (d_0_n_) + (1)
            s = (s) + (d_0_n_)
        return s

if __name__ == '__main__':  
    N = 5
    result = default__.Sum(N)
    print(f"The sum of all integers from 1 to {N} is: {result}")
