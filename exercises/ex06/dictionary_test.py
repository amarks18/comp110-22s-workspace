"""File to test dictionary functions."""

__author__ = "730401929"

from dictionary import invert, favorite_color, count


def test_invert_one() -> None:
    """Test of dict with one pair."""
    assert invert({"tar": "heels"}) == {"heels": "tar"}


def test_invert_two() -> None:
    """Test of regular dict."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_three() -> None:
    """Test of regular dict."""
    assert invert({"Anna": "Marks", "Reese": "Layh"}) == {"Marks": "Anna", "Layh": "Reese"}


def test_favorite_color_one() -> None:
    """Test of regular dict."""
    assert favorite_color({"Anna": "blue", "Reese": "green", "Mikaela": "yellow", "Morgan": "blue"}) == "blue"


def test_favorite_color_two() -> None:
    """Test of dict with same amount of two fav colors."""
    assert favorite_color({"Anna": "blue", "Reese": "green", "Mikaela": "yellow"}) == "blue"


def test_favorite_color_three() -> None:
    """Test of dict with one pair."""
    assert favorite_color({"Anna": "blue"}) == "blue"


def test_count_one() -> None: 
    """Test of list with no repeats."""
    assert count(["Anna", "Reese", "Mikaela"]) == {"Anna": 1, "Reese": 1, "Mikaela": 1}


def test_count_two() -> None: 
    """Test of list with repeats."""
    assert count(["Anna", "Anna", "Reese", "Mikaela"]) == {"Anna": 2, "Reese": 1, "Mikaela": 1}


def test_count_three() -> None:
    """Test of list with one item."""
    assert count(["Anna"]) == {"Anna": 1}