"""CQ04"""

# defining zip
def zip(list1: list[str], list2: list[int]) -> dict:
    # concatenating empty list
    result: dict[str, int] = {}
    # at least one empty list
    empty: list = {}
    if not list1 or not list2:
        return {}
    # len of lists are unequal
    if len(list1) != len(list2):
        return {}
    # lists are not empty or unequal, returning dict[str, int]
    else:
        new_result =[list1, list2]
        return dict(new_result)
    
def main() -> None:
    list1: list[str]
    list2: list[int]

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
       
    
    