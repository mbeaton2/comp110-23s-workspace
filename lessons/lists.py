"""Practice with lists."""

grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1] = "cereal"
grocery_list.pop(2)
grocery_list.pop(1)
grocery_list.pop(0)
print(grocery_list)