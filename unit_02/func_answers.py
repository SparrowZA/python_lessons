# We need the maths library for example 1
# here we import the maths library
import math


def compute_hypotenuse(side_1: float, side_2: float) -> float:
    """ This function take 2 length of a right triangle
    and computes the hypotenuse
    """
    # This is one way to compute the hypotenuse
    # hypot = math.hypot(side_1, side_2)

    # Another way to compute the hypotenuse
    hypot = math.sqrt(side_1 ** 2 + side_2 ** 2)
    return hypot

def calculate_shipping_cost(item_count: int) -> float:
    """ This function takes the number of items
    and computes the shipping cost
    """
    # Define the base cost and additional item cost
    base_cost: float = 10.95
    additional_item_cost: float = 2.95

    # Set the shipping cost to a default value
    shipping_cost: float = 0.0

    if item_count == 1:
        # We apply the base shipping cost for the first item
        shipping_cost = base_cost
    elif item_count > 1:
        # We apply the base cost plus the additional item cost
        shipping_cost = base_cost + (item_count - 1) * additional_item_cost
    return shipping_cost

def get_median(value_1: float, value_2: float, value_3: float) -> float:
    """ This function takes three values
    and returns the median value
    """
    # Using if statements to find the median
    median = 0.0
    if (value_1 >= value_2) and (value_1 <= value_3) or (value_1 <= value_2) and (value_1 >= value_3):
        median = value_1
    elif (value_2 >= value_1) and (value_2 <= value_3) or (value_2 <= value_1) and (value_2 >= value_3):
        median = value_2
    else:
        median = value_3

    # A more mathematical way to find the median
    # median = sum of all the values - min value - max value
    median = value_1 + value_2 + value_3 - min(value_1, value_2, value_3) - max(value_1, value_2, value_3)
    return median

def capitalize_string(input_string: str) -> str:
    """ This function takes a string and returns the string
    with the first and last letter capitalized
    """
    # Define a result string
    result: str = ""

    # What if the string is empty or has only one character?
    if len(input_string) == 0:
        result = input_string
    elif len(input_string) == 1:
        result = input_string.upper()
    else:
        # input string  -> "hello"
        # result = input_string[0].upper()
        # result        -> H
        # result = result + input_string[1:-1]
        # result        -> Hell
        # result = result + input_string[-1].upper()
        # result        -> HellO
        # All in one line
        result = input_string[0].upper() + input_string[1:-1] + input_string[-1].upper()
    return result

def main():
    # 1. Compute the Hypotenuse
    side_1: float = 3.0
    side_2: float = 4.0
    hypotenuse: float = compute_hypotenuse(side_1, side_2)
    print(f"The hypotenuse of a triangle with side lengths of {side_1} and {side_2} is: {hypotenuse}")

    # 2. Shipping Calculator
    item_count: int = int(input("Enter the number of items to ship: "))
    shipping_cost: float = calculate_shipping_cost(item_count)
    print(f"The shipping cost for {item_count} items is: ${shipping_cost:.2f}")

    # 3 Median of Three Values
    median: float = get_median(10.5, 7.2, 8.3)
    print(f"The median of the values 10.5, 7.2, and 8.3 is: {median}")

    # 4 Capitalize It
    user_string: str = "Creative"
    capitalized_string: str = capitalize_string(user_string)
    print(f"The string '{user_string}' with the first and last letters capitalized is: '{capitalized_string}'")

if __name__ == "__main__":
    # We do this to ensure that there is no code that runs
    # in the global scope.
    main()
