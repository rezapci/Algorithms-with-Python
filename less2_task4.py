# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Find the sum of n elements of the following series of numbers: 1 -0.5 0.25 -0.125 ...
# The number of items (n) is entered from the keyboard.

print( "Find the sum of a certain number of elements in a series of numbers")
n =  int (input("Enter the number of elements:"))

x = 1
y =  0

for i in range(n):
    y = x + y
    x = x / -2
print("amount {}".format(y))
