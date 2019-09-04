# Reference to Flowcharts:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# The user enters the number of the letter in the alphabet.
# Determine which letter it is.

print ( " Define a letter by its number " )

x =  int ( input ( " Enter the letter number " ))

letter = ord('a') + x - 1

print ( " This is the letter: {} " .format ( chr (letter)))
