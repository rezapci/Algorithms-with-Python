# Reference to Flowcharts:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Based on the lengths of the three segments entered by the user, determine the possibility of the existence of a triangle composed of these segments.
# If such a triangle exists, then determine whether it is versatile, isosceles or equilateral.

print ( " Define the possibility of the existence of a triangle and its type " )
a =  int ( input ( " Enter the length of the first segment: " ))
b =  int ( input ( " Enter the length of the second segment: " ))
c =  int ( input ( " Enter the length of the third segment: " ))

if a + b <= c or a + c <= b or b + c <= a:
    print ( " Such a triangle does not exist " )
elif a != b and a != c and b != c:
    print ( " Triangle versatile " )
elif a == b == c:
    print ( " Triangle equilateral " )
else:
    print ( " Isosceles Triangle " )
