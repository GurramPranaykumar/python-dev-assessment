def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        print("Warning: Empty list provided. Returning 0.")
        return 0

def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds.")
        return None
    except TypeError:
        print("Error: Provided input is not a list.")
        return None

example_list = [10, 20, 30]

print(get_list_element(example_list, 1))   # valid → 20
print(get_list_element(example_list, 5))   # out-of-bounds → error message
print(get_list_element("not a list", 0))   # wrong type → error message