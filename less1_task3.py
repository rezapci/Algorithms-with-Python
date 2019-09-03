# Reference to Flowcharts:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Using the coordinates of two points entered by the user, derive the equation of a line passing through these points.

print ( "We derive the equation of a line passing through given points " )
print ( " Enter the coordinates of the first point: " )
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print ( " Enter the coordinates of the second point: " )
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2

print ( " The equation of a line passing through these points: y = {} * x + {} " .format (k, b))
