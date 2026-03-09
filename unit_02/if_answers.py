# ==================================================
# 1.
# NOTE: These solutions don't take into account uppercase letters
# ==================================================
character: str = input("Please enter a letter:")
# Method #1: Using multiple else if statements
if character == 'a':
    print("This is a vowel")
elif character == 'e':
    print("This is a vowel")
elif character == 'i':
    print("This is a vowel")
elif character == 'o':
    print("This is a vowel")
elif character == 'u':
    print("This is a vowel")
elif character == 'y':
    print("Y is a vowel, and sometimes a consonant")
else:
    print("The letter is a consonant")

# Method #2: Using AND and OR operators
if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print("This is a vowel")
elif character == 'y':
    print("Y is a vowel, and sometimes a consonant")
else:
    print("The letter is a consonant")

# Method #3: Using lists
VOWELS = ['a', 'e', 'i', 'o', 'u']

if character in VOWELS:
    print("This is a vowel")
elif character == 'y':
    print("Y is a vowel, and sometimes a consonant")
else:
    print("The letter is a consonant")

# ==================================================
# 2.
# ==================================================
bank_note: int = int(input("Please enter amount:"))
if bank_note == 1:
    print("George Washington")
elif bank_note == 2:
    print("Thomas Jefferson")
elif bank_note == 5:
    print("Abraham Lincoln")
elif bank_note == 10:
    print("Alexander Hamilton")
elif bank_note == 20:
    print("Andrew Jackson")
elif bank_note == 50:
    print("Ulysses S. Grant")
elif bank_note == 100:
    print("Benjamin Franklin")
else:
    print("There is no note for that amount")

# ==================================================
# 3.
# ==================================================
magnitude: float = float(input("Please enter amount:"))
# Note the great than or equal to
if magnitude < 2.0:
    print("This is a micro Earthquake")
elif magnitude >= 2.0 and magnitude < 3.0:
    print("This is a very minor Earthquake")
elif magnitude >= 3.0 and magnitude < 4.0:
    print("This is a minor Earthquake")
elif magnitude >= 4.0 and magnitude < 5.0:
    print("This is a light Earthquake")
elif magnitude >= 5.0 and magnitude < 6.0:
    print("This is a moderate Earthquake")
elif magnitude >= 6.0 and magnitude < 7.0:
    print("This is a strong Earthquake")
elif magnitude >= 7.0 and magnitude < 8.0:
    print("This is a major Earthquake")
elif magnitude >= 8.0 and magnitude < 10.0:
    print("This is a great Earthquake")
elif magnitude >= 10.0:
    print("This is a meteoric Earthquake")
else:
    print("The input is invalid")
