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
    def iter__copy(default___T, s):
        t: _dafny.Array = _dafny.Array(None, 0)
        nw0_ = _dafny.Array(default___T(), (s).length(0))
        t = nw0_
        d_0_i_: int
        d_0_i_ = 0
        while (d_0_i_) < ((s).length(0)):
            (t)[(d_0_i_)] = (s)[d_0_i_]
            d_0_i_ = (d_0_i_) + (1)
        return t


if __name__ == "__main__":
    s = _dafny.Array(0, 5)  # create an array of size 5 with all elements initialized to 0
    for i in range(5):
        s[i] = i + 1  # populate array with values [1, 2, 3, 4, 5]
    
    copied_array = default__.iter__copy(int, s)
    print("Original array:", [s[i] for i in range(s.length(0))])
    print("Copied array:", [copied_array[i] for i in range(copied_array.length(0))])

