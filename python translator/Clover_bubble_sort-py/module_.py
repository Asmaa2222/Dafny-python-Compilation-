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
    def BubbleSort(a):
        d_0_i_: int
        d_0_i_ = ((a).length(0)) - (1)
        while (d_0_i_) > (0):
            d_1_j_: int
            d_1_j_ = 0
            while (d_1_j_) < (d_0_i_):
                if ((a)[d_1_j_]) > ((a)[(d_1_j_) + (1)]):
                    index0_ = (d_1_j_) + (1)
                    rhs0_ = (a)[(d_1_j_) + (1)]
                    rhs1_ = (a)[d_1_j_]
                    lhs0_ = a
                    lhs1_ = d_1_j_
                    lhs2_ = a
                    lhs3_ = (d_1_j_) + (1)
                    lhs0_[lhs1_] = rhs0_
                    lhs2_[lhs3_] = rhs1_
                d_1_j_ = (d_1_j_) + (1)
            d_0_i_ = (d_0_i_) - (1)

if __name__ == "__main__":
    # Create an unsorted array
    a = _dafny.Array([64, 34, 25, 12, 22, 11, 90])
    a=[64, 34, 25, 12, 22, 11, 90]
    
    # Call the BubbleSort function
    default__.BubbleSort(a)
    
    # Print the sorted array
    print(f"Sorted array: {a.data}")