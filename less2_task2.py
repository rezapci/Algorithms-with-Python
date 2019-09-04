# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Count the even and odd digits of the entered natural number.
# For example, if the number 34560 is entered, then he has 3 even numbers (4, 6 and 0) and 2 odd numbers (3 and 5).

print ( " Count the odd and even numbers in a natural number " )
num =  int ( input ( " Enter a positive integer: " ))

even = 0
odd = 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num //=  10
print ( " Even {} , odd {} " .format (even, odd))
