# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Calculate how many times a certain digit occurs in the entered sequence of numbers.
# The number of input numbers and the number to be calculated are set by keyboard input.

print ( " Count how many times the desired digit occurs in a sequence of numbers. " )

x =  int ( input ( " Enter the number of numbers in the sequence: " ))
y =  int ( input ( " Enter the search digit: " ))

i = 1
j = 0

while i < x+1:
    num = int(input("Enter the Number № {}".format(i)))
    if num == y:
        j += 1
        i += 1
    else:
        i += 1
else:
    print ( "The search digit has occurred {} times (s) " .format (j))
