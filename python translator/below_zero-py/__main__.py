# Dafny program below_zero.dfy compiled into Python
import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_ as module_
from module_ import default__
import _dafny as _dafny

def main():
    test_data = [100, -50, -75, 20, -100]  # Example data
    result = default__.BelowZero(test_data)
    print(f"Does the balance fall below zero? {result}")

if __name__ == "__main__":
    main()
