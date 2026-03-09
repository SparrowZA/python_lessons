# ===================
# 1. Average
# ===================
input_val: int = int(input("Enter a positive integer (0 to stop): "))
# We use a while loop here because it's a indefinite loop
# We don't know how many numbers the user will enter
total: int = 0
count: int = 0
average: float = 0.0
while input_val != 0:
    total += input_val
    count += 1
    input_val = int(input("Enter a positive integer (0 to stop): "))

# Using the total and count to compute the average
if count > 0:
    average = total / count
else:
    average = 0.0
print(f"The average of the entered numbers is: {average}")

# ===============================
# 2. Temperature Conversion Table
# ===============================
print("Celsius to Fahrenheit conversion table:")
print("Celsius  Fahrenheit")
# There is a third argument in range() which is the step
# It defines the increment between each value in the range
for temp in range(0, 101, 10):
    fahrenheit: float = (temp * 9/5) + 32
    print(f"{temp:3}C = {fahrenheit:6.1f}F")

# ==================
# 3. Heads and tails
# ==================
# We're importing here but this will usually be at the top of the file
import random


total_flips: int = int(input("Enter the number of times to flip the coin: "))
heads_count: int = 0
tails_count: int = 0
for _ in range(total_flips):
    flip: int = random.randint(0, 1)  # 0 for heads, 1 for tails
    if flip == 0:
        heads_count += 1
    else:
        tails_count += 1
print(f"Heads: {heads_count}, Tails: {tails_count}")

# ==========
# Start tree
# ==========
# start at 1 and set the 
for i in range(1,11):
    print('*' * i)
