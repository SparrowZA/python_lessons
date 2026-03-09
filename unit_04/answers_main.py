import math
from answers import (sum_list,
                    average_length,
                    create_random_number_list,
                    count_strings_with_ending,
                    reverse_list,
                    get_average
                    )


def main() -> None:
    # Exercise #01
    print("---Exercise #01")
    monthly_costs: list[float] = [121.98, 879.45, 19.00, 23.99, 83.01, 43.22]
    total_cost = sum_list(monthly_costs)
    # Note the use of :.2f to format the float to 2 decimal places
    print(f"Total monthly cost: ${total_cost:.2f}")

    # Exercise #02
    print("---Exercise #02")
    number_list: list[int] = [
            155, 446, 753, 368, 173, 459, 858, 772, 826, 54, 114, 925, 869,
            220, 306, 293, 907, 169, 662, 302, 157, 133, 298, 383, 67, 82, 972,
            803, 574, 663, 519, 48, 468, 685, 202, 950, 35, 939, 906, 845, 210,
            7, 422, 152, 393, 247, 337, 91, 68, 571, 313, 553, 77, 350, 529,
            694, 997, 936, 642, 135, 629, 424, 224, 531, 813, 46, 781, 504,
            648, 944, 477, 834, 666, 653, 734, 369, 926, 31, 63, 665, 352, 142,
            66, 521, 851, 389, 912, 38, 402, 355, 192, 913, 824, 250, 385, 917,
            933, 968, 562, 61
        ]
    # When using data that is in a list and you want to analyse it. It's
    # common to sort the list first.

    # Python make that easy with the sort() method.
    number_list.sort()
    maximum = number_list[-1]
    minimum = number_list[0]
    print(f"Max: {maximum}, Min: {minimum}")

    # You can also use the built-in functions max() and min()
    max2 = max(number_list)
    min2 = min(number_list)
    print(f"Max: {max2}, Min: {min2}")

    # Doing it the long way
    print("---Exercise #03")
    maximum = 0
    minimum = 0
    for number in number_list:
        if number > maximum:
            maximum = number
        if number < minimum or minimum == 0:
            minimum = number
    print(f"Max: {maximum}, Min: {minimum}")

    # Exercise #03
    print("---Exercise #04")
    word_list: list = [
        "apple", "banana", "cherry", "delta", "eagle", "forest", "giraffe",
        "honey", "island", "jungle", "kangaroo", "lemon", "monkey", "nectar",
        "orange", "peach", "quartz", "river", "sunset", "tiger", "umbrella",
        "violet", "water", "xenon", "yellow", "zebra", "waiter", "wanted"
    ]
    avg_length = average_length(word_list)
    print(f"Average word length: {avg_length:.2f}")

    # Exercise #04
    print("---Exercise #04")
    random_numbers = create_random_number_list()
    print(random_numbers)

    # Exercise #05
    print("---Exercise #05")
    word_list = [
        "apple", "banana", "cherry", "delta", "eagle", "forest", "giraffe",
        "honey", "island", "jungle", "kangaroo", "lemon", "monkey", "nectar",
        "orange", "peach", "quartz", "river", "sunset", "tiger", "umbrella",
        "violet", "water", "xenon", "yellow", "zebra", "waiter", "wanted"
    ]
    ending: str = "set"
    print(f"Words ending with '{ending}': {count_strings_with_ending(word_list, ending)}")
    ending = "a"
    print(f"Words ending with '{ending}': {count_strings_with_ending(word_list, ending)}")
    ending = "wa"
    print(f"Words ending with '{ending}': {count_strings_with_ending(word_list, ending)}")
    ending = ""
    print(f"Words ending with '{ending}': {count_strings_with_ending(word_list, ending)}")

    # Exercise #06
    print("---Exercise #06")
    original_list: list[int] = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(original_list)
    print(f"Reversed list: {reversed_list}")

    # Exercise #07
    print("---Exercise #07")
    rf_board: list[list[int]] = [
        [
            48, 90, 52, 23, 93, 39, 26, 12, 53, 63, 88, 37, 80, 34, 16, 81, 22, 40,
            27, 21, 68, 14, 80, 90, 93, 22, 23, 66, 3, 47, 13, 72, 52, 13, 48, 37, 33,
            73, 5, 15, 93, 55, 58, 83, 25, 88, 83, 77, 11, 90
        ],
        [
            32, 33, 11, 2, 67, 29, 29, 77, 55, 65, 33, 90, 54, 98, 47, 53, 38, 24, 78,
            34, 55, 73, 33, 10, 97, 6, 93, 30, 32, 57, 3, 59, 50, 51, 19, 87, 83, 62,
            71, 68, 83, 20, 35, 61, 37, 61, 17, 32, 75, 4
        ],
        [
            52, 5, 68, 90, 67, 4, 30, 0, 8, 32, 6, 19, 69, 10, 34, 70, 19, 84, 89, 18,
            11, 4, 72, 23, 70, 48, 48, 62, 93, 71, 57, 69, 10, 6, 85, 9, 32, 85, 79,
            26, 18, 66, 63, 92, 51, 56, 74, 74, 47, 34
        ],
        [
            14, 47, 24, 12, 39, 59, 4, 89, 7, 12, 62, 11, 63, 96, 52, 92, 83, 88, 19,
            58, 90, 33, 17, 20, 46, 4, 63, 71, 34, 92, 41, 46, 96, 10, 17, 86, 66,
            41, 69, 57, 8, 61, 20, 73, 38, 16, 58, 94, 46, 87
        ]
    ]
    # i
    for s_param in rf_board:
        average = get_average(s_param)
        print(f"The average is: {average}")

    # ii
    results: list = []
    for index in range(len(rf_board[0])):
        temp_value = math.sqrt(rf_board[3][index] + rf_board[0][index])
        results.append(temp_value)
    print(f"Results for ii: {results}")

    # iii
    results = []
    for index in range(len(rf_board[0])):
        results.append(rf_board[0][index] - rf_board[2][index])
    print(f"Results for iii: {results}")

if __name__ == "__main__":
    main()
