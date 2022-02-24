"""File to test unit tests."""

__author__ = "730401929"

from utils import only_evens, sub, concat 


def test_only_evens_one() -> None: 
    """Test of regular list."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_two() -> None: 
    """Test of list with no evens."""
    assert only_evens([1, 3, 9, 7]) == []


def test_only_evens_three() -> None: 
    """Test of empty list."""
    assert only_evens([]) == []


def test_sub_one() -> None:
    """Test of empty list."""
    assert sub([], 1, 1) == []


def test_sub_two() -> None:
    """Test of list with negative starting int value."""
    assert sub([1, 1, 1, 1], -5, 1) == [1]


def test_sub_three() -> None: 
    """Test of regular list with ascending int values."""
    assert sub([1, 2, 3, 4], 1, 2) == [1, 2]


def test_concat_one() -> None: 
    """Test of regular list with ascending int values."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None: 
    """Test of empty lists."""
    assert concat([], []) == []


def test_concat_three() -> None: 
    """Test of lists of different lengths."""
    assert concat([5, 4], [3, 2, 1]) == [5, 4, 3, 2, 1]