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
    def sum(s, n):
        d_0___accumulator_ = 0
        while True:
            with _dafny.label():
                if ((len(s)) == (0)) or ((n) == (0)):
                    return (0) + (d_0___accumulator_)
                elif True:
                    d_0___accumulator_ = (d_0___accumulator_) + ((s)[0])
                    in0_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                    in1_ = (n) - (1)
                    s = in0_
                    n = in1_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def BelowZero(ops):
        result: bool = False
        result = False
        d_1_t_: int
        d_1_t_ = 0
        hi0_ = len(ops)
        for d_2_i_ in range(0, hi0_):
            d_1_t_ = (d_1_t_) + ((ops)[d_2_i_])
            if (d_1_t_) < (0):
                result = True
                return result
        return result

if __name__ == '__main__':
    ops = [100, -50, -75, 20, -100]
    # Using the original class
    print(default__.BelowZero(ops))  # Output: True

