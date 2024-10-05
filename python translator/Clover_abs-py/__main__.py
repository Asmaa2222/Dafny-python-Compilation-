# Dafny program Clover_abs.dfy compiled into Python
import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count
import module_ as module_
from module_ import default__
import _dafny as _dafny

if __name__ == '__main__':
    test_values = [-10, 0, 15, -7, 20]
    # Applying the original Abs function to each test value
    results_original = {val: default__.Abs(val) for val in test_values}
    print(results_original)