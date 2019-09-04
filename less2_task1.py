# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Write a program that will add, subtract, multiply or divide two numbers.
# Numbers and the operation sign are entered by the user. After the calculation is complete, the program should not end,
# and should request new data for calculations.
# Program termination should be performed when the character '0' is entered as an operation sign.
# If the user enters an incorrect character (not '0', '+', '-', '*', '/'), then the program should inform him of the error and
# request the operation sign again.
# Also inform the user about the impossibility of dividing by zero if he entered 0 as a divisor.


print ( " Enter two numbers and the operation on them: " )
operation = None

while operation != "0":
    number1 = float(input("first number: "))
    number2 = float(input("second number: "))
    operation =  input ( " What will we do with them (+, -, *, /): " )

    if operation == "+":
        print(number1 + number2)
    elif  operation == "-":
        print(number1 - number2)
    elif operation == "*":
        print(number1 * number2)
    elif operation == "/":
        if number2 == 0:
            print ( " Division by zero is not possible! " )
        else:
            print(number1 / number2)
    else:
        print ( " Unknown operation " )
else:
    print ( " Goodbye " )
