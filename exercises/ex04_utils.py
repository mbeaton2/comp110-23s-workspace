"""Utility Functions Exercise!"""
__author__: "730480912"
  
# defining all
# all is a bool, so return bool will return True or False depending on if the integers in the list and single integer are the same

def all(integer_list: list[int], single_integer: int) -> bool:
    if len(integer_list) == 0:
        return False
    number: int = 0
    while number < len(integer_list):
        if single_integer == integer_list[number]: 
            number += 1
            return False 
        else:
            if single_integer != integer_list[number]:
                return True 
        
# defining max to return the max number in a list of numbers 

def max(input: list) -> int:
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    if len(input) != 0:
        return max(input)

# defining is_equal to determing is two lists are equal to one another
def is_equal(list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return False
    idx: int = 0 
    if list1[idx] != list2[idx]:
        return False
    return True 