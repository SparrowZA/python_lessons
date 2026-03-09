import random


def sum_list(numbers: list[float]) -> float:
    """Returns the sum of a list of numbers."""
    total: float = 0
    for number in numbers:
        total += number
    return total

def average_length(words: list[str]) -> float:
    """Returns the average length of words in a list."""
    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length / len(words)

def create_random_number_list() -> list[int]:
    """Creates a list of 100 unique random numbers between 1-1000."""
    result: list[int] = []
    history: list[int] = []
    count: int = 0
    while count < 100:
        number = random.randint(1, 1000)
        if number not in history:
            result.append(number)
            history.append(number)
            count += 1
    return result

def count_strings_with_ending(words: list[str], ending: str) -> int:
    """Counts the number of strings that end with a specific ending."""
    count: int = 0
    for word in words:
        # Using the built-in str.endswith() method
        if word.endswith(ending):
            count += 1

        # Without using the built-in method
        # check if the ending is not longer than the word
        # then compare the end of the word with the ending
        # if len(word) >= len(ending) and word[-len(ending):] == ending:
        #     count += 1
    return count

def reverse_list(original: list[int]) -> list[int]:
    """Returns a list of the same values but the order of the list is reversed."""
    new_list: list[int] = []
    # Method 1
    for item in original:
        new_list.insert(0, item)

    # Method 2
    for i in range(len(original) - 1, -1, -1):
        new_list.append(original[i])

    # Method 3
    temp: int = 0
    list_length: int = len(original)
    for i in range(list_length // 2):
        temp = original[i]
        original[i] = original[list_length - 1 - i]
        original[list_length - 1 - i] = temp
    return new_list

def get_average(numbers: list) -> float:
    """ takes a list of numbers and returns the average value of the list back """
    total: float = 0.0
    count: int = 0
    for value in numbers:
        total += value
        count += 1
    return total / count
