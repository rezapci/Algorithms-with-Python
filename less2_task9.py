# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Among the natural numbers that were entered, find the largest in the sum of the digits.
# Display this number and the sum of its digits.

print ( " Count the largest number of digits " )

number = int(input("Enter the Number: "))
max_number = 0
max_sum = 0

while number != 0:
    i = 0
    j = number
    while number > 0:
        i = i + number % 10
        number //= 10
    if i > max_sum:
        max_sum = i
        max_number = j

    number = int(input("Enter the Number: "))
else:
    print ( "The maximum number of digits is {} , the sum of its numbers is {} " .format (max_number, max_sum))
