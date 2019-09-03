# Ссылка на блоксхемы:
# https://drive.google.com/file/d/1MxReXi2rVMhkFsbYynmA2gXycnVpdrwP/view?usp=sharing

# Perform logical bitwise operations "AND", "OR", etc. on the numbers 5 and 6.
# Perform a bitwise shift over the number 5 to the right and left by two characters.
# Explain the result.

a = 5
b = 6

print("{} & {} = {} ({})".format(a, b, a & b, bin(a & b)))

print("{} | {} = {} ({})".format(a, b, a | b, bin(a | b)))

print("Побитовый сдвиг числа {} вправо на два знака: {} ({})".format(a, a >> 2, bin(a >> 2)))

print("Побитовый сдвиг числа {} влево на два знака: {} ({})".format(a, a << 2, bin(a << 2)))
