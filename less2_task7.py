# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Write a program proving or verifying,
# that for the set of natural numbers the equality holds: 1 + 2 + ... + n = n (n + 1) / 2, where n is any natural number.

print ( " Let's check if the equality is of the form 1 + 2 + ... + n = n (n + 1) / 2 " )

n =  int ( input ( " Enter a positive integer n: " ))
x = 0

for i in range(1, n+1):
    x = i + x

y = n * (n +  1 ) //  2

if x == y:
    print ( " Equality Proved " )
else:
    print ( " Equality not proven " )
