# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Form from the entered number the reverse in the order of the numbers included in it and display it on the screen.
# For example, if the number 3486 is entered, then you need to print the number 6843.

print("Form the Inverse Number")
number = input("Enter the number: ")

# One could solve without loops like this:

# Subsidized = number [:: - 1]
# Print (the situation)

# Or after two cycles like this:

number = int(number)
won = []

while number>0:
    rebmun.append(number % 10)
    number //= 10

for num in rebmun:
    print(num, end='')
