# Reference to Flowcharts:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# The user enters two letters.
# Determine where in the alphabet they stand and how many letters are between them.

print ("Enter two letters of the Latin alphabet")
x =  ord (input("First letter:"))
y =  ord (input("Second letter:"))

px = x - ord('a') + 1
py = y - ord('a') +  1

print("Positions of these letters:{}and{}".format(px, py))

l = abs(px - py)
print("Between them {} letters(s)".format(l)
