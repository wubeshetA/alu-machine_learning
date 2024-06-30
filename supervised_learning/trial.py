my_list = [1, "two", 3.0, [4, 5], 1]

for i, item in enumerate(my_list):
    print(f"Element {i} is at memory address {id(item)}")
