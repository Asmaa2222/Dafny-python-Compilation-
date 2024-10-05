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
    def maxArray(a):
        m: int = int(0)
        m = (a)[0]
        d_0_index_: int
        d_0_index_ = 1
        while (d_0_index_) < ((a).length(0)):
            m = (m if (m) > ((a)[d_0_index_]) else (a)[d_0_index_])
            d_0_index_ = (d_0_index_) + (1)
        return m

if __name__ == "__main__":
    a = _dafny.Array(0, 5)  # create an array of size 5 initialized with 0
    
    # Populate array a with values
    for i in range(5):
        a[i] = i * 3  # [0, 3, 6, 9, 12]
    
    # Call the maxArray function
    result = default__.maxArray(a)
    
    # Print the result
    print("Array a:", [a[i] for i in range(a.length(0))])
    print("Max value in array a:", result)