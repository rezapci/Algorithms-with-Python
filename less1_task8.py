# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

print ( " Determine if a year is a leap year " )
year = int(input("Enter the year: "))

if year % 4 != 0:
    print ( "The year is not a leap year " )
elif year % 100 == 0:
    if year % 400 == 0:
        print ( " Leap year " )
    else:
        print ( "The year is not a leap year " )
else:
    print ( " Leap year " )
