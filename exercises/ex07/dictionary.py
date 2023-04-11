"""Dictionary Functions!"""

___author___: "730480912"

def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
        """Will invert the keys and values in a dictionary."""
        my_inverted_dictionary = {}
        assert len(my_dictionary) == len(my_inverted_dictionary)
        if len(my_dictionary) != len(my_inverted_dictionary):
            return AssertionError
        for [key, value] in my_dictionary.keys():
            key1: int = 0
            key2: int = 0
            if key1 in my_inverted_dictionary == key2 in my_inverted_dictionary:
                raise KeyError("Stop repeating keys! ")
            [key] = my_inverted_dictionary
        return my_inverted_dictionary

def favorite_color(name_colors: dict[str, str]) -> str:
    """Will return the most common color in a dictionary."""
    the_colors = {}
    for color in name_colors.values():
        if color in the_colors: 
            the_colors[color] += 1
        else: 
            the_colors[color] = 1
    popular_color = max(the_colors.keys())
    return popular_color 
          
def count(frequencies: list[str]) -> dict[str, int]:
    """Will count the occurences of a number in a list and record it in a dictionary."""
    counting = {}
    for elem in frequencies:
        if elem in counting:
            counting[elem] += 1
        else:
            counting[elem] = 1
    return counting 
