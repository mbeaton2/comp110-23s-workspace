"""CQ04"""

def main() -> None:
    list1: list[str]
    list2: list[int]

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    if len(list1) != len(list2):
        result == {}
        return result
    if not list1 or not list2:
        result == {}
        return result 
    for i in range(len(list1)):
        result[list1[i]] = list2[i]
    return result

