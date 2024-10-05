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
    def arraySum(a, b):
        c: _dafny.Array = _dafny.Array(None, 0)
        nw0_ = _dafny.Array(int(0), (a).length(0))
        c = nw0_
        d_0_i_: int
        d_0_i_ = 0
        while (d_0_i_) < ((a).length(0)):
            (c)[(d_0_i_)] = ((a)[d_0_i_]) + ((b)[d_0_i_])
            d_0_i_ = (d_0_i_) + (1)
        return c

if __name__ == "__main__":
    a = _dafny.Array(0, 5)  # create an array of size 5 initialized with 0
    b = _dafny.Array(0, 5)  # create another array of size 5 initialized with 0
    
    # Populate arrays a and b with values
    for i in range(5):
        a[i] = i + 1  # [1, 2, 3, 4, 5]
        b[i] = (i + 1) * 2  # [2, 4, 6, 8, 10]
    
    # Call the arraySum function
    result = default__.arraySum(a, b)
    
    # Print the result
    print("Array a:", [a[i] for i in range(a.length(0))])
    print("Array b:", [b[i] for i in range(b.length(0))])
    print("Array sum:", [result[i] for i in range(result.length(0))])