"""Dictionary Functions Tests!"""

___author___: "730480912"

import pytest 

    from exercises.ex07.dictionary import invert
    """Testing invert."""
    def test_invert():

        # edge case: returns empty 
        inversion = {}
        expected_inversion = {}
        assert invert(inversion) == expected_inversion

        # use case: and values inverted
        assert invert({"a": "1", "b": "2", "c": "3"}) == ({"1": "a", "2": "b", "3": "c"}) 

        # use case: repeated value produces a KeyError 
        assert invert({"a": "1", "b": "1", "c": "3"}) == KeyError 
        return KeyError 

    from exercises.ex07.dictionary import favorite_color
    """Testing favorite_color."""
    def test_favorite_color():

        # edge case: everyone has the same favorite color 
        assert favorite_color({"Mikayla": "green", "Emma": "green", "Ryann": "green"}) == "green"

        # use case: favorite color properly returned 
        assert favorite_color({"Mikayla": "green", "Emma": "blue", "Kiley": "blue"}) == "blue"

        # use case: tie for favorite color returns the color that came first in the dictionary 
        result = favorite_color[0]
        assert favorite_color({"Mikayla": "green", "Emma": "blue", "Ryann": "blue", "Caity": "green"}) == "green"
        return result 

    from exercises.ex07.dictionary import count 
    """Testing count."""
    def test_count(): 
        elem = ("green", "blue", "purple")

        # edge case: returns empty
        counts = []
        expected_counts = {}
        assert count(counts) == expected_counts

        # use case: counting 
        assert count(["green", "green", "blue", "purple"]) == ({"green": 2, "blue": 1, "purple": 1})

        # use case: list of the same number
        assert count(["blue", "blue", "blue", "blue"]) == ({"blue": 4})
