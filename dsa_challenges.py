# Function 1: Filter and sort even numbers

def filter_and_sort_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)

# Function 2: Count character frequency (case-insensitive)

def count_character_frequency(text):
    frequency = {}
    text = text.lower()

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

# Example tests
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(filter_and_sort_evens(numbers))

text = "Hello World"
print(count_character_frequency(text))
