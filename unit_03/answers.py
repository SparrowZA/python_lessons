import random

from TextExample import ChapterOne


def random_password_generator():
    """ Exercise #01
    Generates a random password of length 7 to 10 characters."""
    password: str = ""
    password_length = random.randrange(7, 11)
    for i in range(password_length):
        character = chr(random.randrange(33, 126))
        password += character
    return password

def check_password(password: str) -> bool:
    """ Exercise #02
    This function will take in a password and check for
     the following criteria
      - 8 characters long
      - At least one upper case letter
      - At least one lower case letter
      - At least one number
    """
    has_upper = False
    has_lower = False
    has_number = False
    if len(password) < 8:
        return False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
    # Use binary logic to return True only if all conditions are met
    return has_upper and has_lower and has_number

def generate_strong_password() -> str:
    """ Exercise #03
    Generates a strong password that meets the criteria defined in check_password."""
    # Set a default value for if the password is strong
    is_strong = False
    password: str = ""
    tries: int = 0
    # Loop until a strong password is generated
    while is_strong == False:
        password = random_password_generator()
        is_strong = check_password(password)
        if not is_strong:
            tries += 1
    print(f"Generated password took {tries} tries")
    return password

def caesar_cipher(data_str: str, offset: int) -> str:
    """ Exercise #04
    This is a basic caesar cipher that will only transpose letters. You could
    expand on this by by having the cipher low ordinal value = 32 (SPACE) and
    the high ordinal value = 126 (~). This will include all the visible
    characters of the ASCII table.
    The offset can be either positive or negative.
    """
    lower_case_low = 97
    lower_case_high = 122
    upper_case_low = 65
    upper_case_high = 90

    # This is an empty string used to add the individual characters to
    result_text = ""

    for letter in data_str:
        # Check if the letter is an uppercase letter
        if ord(letter) >= upper_case_low and ord(letter) <= upper_case_high:
            # Add the offset to the ordinal value
            new_char_int = ord(letter) + offset

            # Check if the new value is above the max value or below the min value
            if new_char_int > upper_case_high:
                new_char_int = upper_case_low + (new_char_int - upper_case_high)
            elif new_char_int < upper_case_low:
                new_char_int = upper_case_high - (upper_case_low - new_char_int)
            result_text += chr(new_char_int)
        # Check if the letter is a lowercase letter
        elif ord(letter) >= lower_case_low and ord(letter) <= lower_case_high:
            # Add the offset to the ordinal value
            new_char_int = ord(letter) + offset
            if new_char_int > lower_case_high:
                new_char_int = upper_case_low + (new_char_int - lower_case_high)
            if new_char_int < lower_case_low:
                new_char_int = upper_case_high - (lower_case_low - new_char_int)
            result_text += chr(new_char_int)
    return result_text


def text_search(text_body: str, search_word: str) -> int:
    """ Exercise #05
    This is a generalized solution to exercise #05. It takes the search word
    and text body as an argument and will return the number of occurances of
    the search word in the text body.
    """
    count = 0
    working_text: str = text_body.lower()
    for word in working_text.split(" "):
        if word == search_word.lower():
            count += 1
    return count
