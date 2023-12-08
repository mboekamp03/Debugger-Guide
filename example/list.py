def print_list_elements(elements):
    for i in range(len(elements)):
        print(f"Element at position {i} is {elements[i+1]}")

my_list = [10, 20, 30, 40, 50]
print("Printing list elements:")
print_list_elements(my_list)
