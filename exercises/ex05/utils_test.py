"""Utils test!"""

__author__: "730480912"

from exercises.ex05.utils import only_evens
"""Testing only_evens"""
def test_only_evens():
    # edge case (this should return an empty list)
    assert only_evens([]) == []
    # use case 1 (no evens found)
    assert only_evens([1, 3, 5, 7]) == []
    # use case 2 (evens found in mixed evens and odds)
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]

from exercises.ex05.utils import sub
"""Testing sub"""
def test_sub():
    # edge case (out of range)
    assert sub([1, 2, 3, 4], 0, 9) == [1, 2, 3, 4]
    # use case 1 (whole list prints)
    assert sub([1, 2, 3, 4], 0, 4) == [1, 2, 3, 4]
    # use case 2 (one integer list so exactly one element will print)
    assert sub([1], 0, 1) == [1]

from exercises.ex05.utils import concat
"""Testing concat"""
def test_concat(): 
    # edge case (empty list in input return an empty list)
    for [] in input(concat([], [])):
        assert concat([], []) == []
    # use case 1 (list 1 concatenated to list 2)
    assert concat([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    # use case 2 (list 1 is empty, list 2 is full -> lists will concatenate but look like only list 2)
    assert concat([], [1, 2, 3, 4]) == [1, 2, 3, 4]
