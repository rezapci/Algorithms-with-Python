# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# The program generates a random integer from 0 to 100.
# The user must guess it in no more than 10 attempts.
# After each unsuccessful attempt, it should be reported more or less than the number entered by the user.
# If after 10 attempts the number is not guessed, then output it.

import random
print ( " Guess the integer from 1 to 100 " )

chance = 0

secret_number = random.randint(1, 101)

while chance < 10:
    number = int(input("Enter the number: "))
    if number == secret_number:
        print("Right!")
        break
    else:
        print ( " Wrong! Try again " )
    chance += 1
else:
    print ( " You ended up trying. A random number was {} " .format (secret_number))
