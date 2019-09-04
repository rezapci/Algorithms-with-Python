# Reference to Flowcharts:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Three different numbers are entered.
# Find which one is medium (more than one, but less than the other).

print ( " Define the average of three " )
a =  int ( input ( " Enter the first number: " ))
b =  int ( input ( " Enter the second number: " ))
c =  int ( input ( " Enter the third number: " ))

if b < a < c or c < a < b:
    print ( " Average {} " .format (a))
elif a < b < c or c < b < a:
    print ( " Average {} " .format (b))
else:
    print ( " Average {} " .format (c))
