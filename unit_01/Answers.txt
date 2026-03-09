#=====================================================
# 1. Mailing Address
#=====================================================
print('Marc Geffroy')
print('21 1st Avenue')
print('7945')
print('Cape Town')
print('Western Cape')
print('South Africa')


#=====================================================
# 2. Hello
#=====================================================
usersName = input('Please enter your name: ')
print('Hello ' + usersName + ', welcome to Python')


#=====================================================
# 3. Area of a room
# Note: All input values are read in as strings. You need to type cast the values to integers
#=====================================================
roomLength = input('Please enter the length of the room: ')
roomWidth = input('Please enter the width of the room: ')
roomArea = int(roomWidth) * int(roomLength)
print('The area of the room is ' + str(roomArea))


#=====================================================
# 4. Tax and Tip
# Note: To get a single quote in a string use the escape character
#=====================================================
bill = input('What is the bill''s total? ')
tax = 5
taxPayment = int(bill) * (tax / 100)
tip = 18
tipPayment = int(bill) * (tip / 100)
total = int(bill) + taxPayment + tipPayment
print('The tax amount on the bill is: ' + str(taxPayment))
print('The tip amount on the bill is: ' + str(tipPayment))
print('The total amount is ' + str(total))


#=====================================================
# 5. Odd or Even
#=====================================================
userNumber = input('Please enter a number above 0: ')
if (int(userNumber) % 2) == 0:
    print('EVEN')
else:
    print('ODD')


#=====================================================
# 6. Sum of the First n Positive Integers
#=====================================================
userNumber = input('Please enter a positive number: ')
sum = ((int(userNumber)) * (int(userNumber) + 1)) / 2
print('Sum of the first n positive integers = ' + str(sum))


#=====================================================
# 7. Fahrenheit to Celsius
#=====================================================
tempFahr = input('Please enter a temperature [''F]')
tempCel = (float(tempFahr) - 32) * (5 / 9)
print(str(tempFahr) + ' degrees fahrenheit is ' + str(tempCel)  + ' Celsius')

tempCel = input('Please enter a temperature in Celsius: ')
tempFahr = (float(tempCel) / (5/9)) + 32
print(str(tempCel) + ' degrees Celsius is ' + str(tempFahr)  + ' fahrenheit')