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
    def append(a, b):
        c: _dafny.Array = _dafny.Array(None, 0)
        nw0_ = _dafny.Array(int(0), ((a).length(0)) + (1))
        c = nw0_
        d_0_i_: int
        d_0_i_ = 0
        while (d_0_i_) < ((a).length(0)):
            (c)[(d_0_i_)] = (a)[d_0_i_]
            d_0_i_ = (d_0_i_) + (1)
        (c)[((a).length(0))] = b
        return c

def test_basic_append():
    initial_array = _dafny.Array(0, 3)
    for i in range(initial_array.length(0)):
        initial_array[i] = i + 1  # [1, 2, 3]
    new_element = 4
    result = default__.append(initial_array, new_element)
    assert result[result.length(0) - 1] == new_element, "Last element should be the new element"
    print("Test Basic Append: Passed")

def test_append_to_empty():
    empty_array = _dafny.Array(0, 0)  # Empty array
    new_element = 1
    result = default__.append(empty_array, new_element)
    assert result.length(0) == 1 and result[0] == new_element, "Array should contain one element, which is the new element"
    print("Test Append to Empty: Passed")

def test_append_to_empty():
    empty_array = _dafny.Array(0, 0)  # Empty array
    new_element = 1
    result = default__.append(empty_array, new_element)
    assert result.length(0) == 1 and result[0] == new_element, "Array should contain one element, which is the new element"
    print("Test Append to Empty: Passed")

def test_append_negative():
    initial_array = _dafny.Array(0, 2)
    initial_array[0], initial_array[1] = 5, 10
    new_element = -3
    result = default__.append(initial_array, new_element)
    assert result[result.length(0) - 1] == new_element, "Last element should be the negative new element"
    print("Test Append Negative: Passed")

def test_append_non_integer():
    initial_array = _dafny.Array(0, 2)
    initial_array[0], initial_array[1] = 1, 2
    new_element = 'test'
    result = default__.append(initial_array, new_element)
    assert result[result.length(0) - 1] == new_element, "Last element should be the non-integer new element"
    print("Test Append Non-Integer: Passed")

if __name__ == "__main__":
    test_basic_append()
    test_append_to_empty()
    test_append_negative()
    test_append_non_integer()

