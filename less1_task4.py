# Reference to Flowcharts:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Write a program that generates within user-specified boundaries:
# random integer;
# random real number;
# random character.
# For each of the three cases, the user sets his range limits.
# For example, if you need to get a random character from 'a' to 'z', then these characters are entered.
# The program should display any character of the alphabet from 'a' to 'z' inclusive.

import random

print ( " Compute a random integer in the specified range " )

min  =  int ( input ( " Enter the minimum number: " ))
max  =  int ( input ( " Enter the maximum number: " ))

integ = random.randint ( 0 , max  -  min ) +  min

print ( " Random integer in this range: {} " .format (integ))

flt = random.random () * ( max  -  min ) +  min

print ( " Random real number in this range: {0 : .2f } " .format (flt))

s1 =  ord ( input ( " Enter the first character: " ))
s2 =  ord ( input ( " Enter the second character: " ))

symbol = random.randint(0, (s2 - s1)) + s1

print ( " Random character in this range: {} " .format ( chr (symbol)))
