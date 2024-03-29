# Reference to Flowcharts:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Perform logical bitwise operations "AND", "OR", etc. on the numbers 5 and 6.
# Perform a bitwise shift over the number 5 to the right and left by two characters.
# Explain the result.

a = 5
b = 6

print("{} & {} = {} ({})".format(a, b, a & b, bin(a & b)))

print("{} | {} = {} ({})".format(a, b, a | b, bin(a | b)))

print ( "The bitwise shift of the number {} to the right by two digits: {} ( {} ) " .format (a, a >>  2 , bin (a >>  2 )))

print ( " Bitwise shift of the number {} to the left by two characters: {} ( {} ) " .format (a, a <<  2 , bin (a <<  2 )))
