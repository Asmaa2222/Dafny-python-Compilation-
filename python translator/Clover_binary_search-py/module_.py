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
    def BinarySearch(a, key):
        n: int = int(0)
        d_0_lo_: int
        d_1_hi_: int
        rhs0_ = 0
        rhs1_ = (a).length(0)
        d_0_lo_ = rhs0_
        d_1_hi_ = rhs1_
        while (d_0_lo_) < (d_1_hi_):
            d_2_mid_: int
            d_2_mid_ = _dafny.euclidian_division((d_0_lo_) + (d_1_hi_), 2)
            if ((a)[d_2_mid_]) < (key):
                d_0_lo_ = (d_2_mid_) + (1)
            elif True:
                d_1_hi_ = d_2_mid_
        n = d_0_lo_
        return n

if __name__ == "__main__":
    a = _dafny.Array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    
    # Call the BinarySearch function
    key = 7
    index = default__.BinarySearch(a, key)
    
    # Print the result
    print(f"BinarySearch for key {key}: Index {index}")
    
    # Test with a key not in the array
    key_not_found = 8
    index_not_found = default__.BinarySearch(a, key_not_found)
    print(f"BinarySearch for key {key_not_found}: Index {index_not_found}")