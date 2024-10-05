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
    def minArray(a):
        r: int = int(0)
        r = (a)[0]
        d_0_i_: int
        d_0_i_ = 1
        while (d_0_i_) < ((a).length(0)):
            if (r) > ((a)[d_0_i_]):
                r = (a)[d_0_i_]
            d_0_i_ = (d_0_i_) + (1)
        return r

if __name__ == "__main__":
    a = _dafny.Array(0, 5)  # create an array of size 5 initialized with 0
    
    # Populate array a with values
    for i in range(5):
        a[i] = i * 3  # [0, 3, 6, 9, 12]
    
    # Call the maxArray function
    result = default__.minArray(a)
    
    # Print the result
    print("Array a:", [a[i] for i in range(a.length(0))])
    print("Min value in array a:", result)