# In the range of natural numbers from 2 to 99, determine how many of them are multiples of any of the numbers in the range from 2 to 9.

print (' Lets calculate how many numbers in the range from 2 to 99 are multiples of any of the numbers in the range from 2 to 9 ' )

arr = [0] * 8

for i in  range (2 , 100):
    for j in range(2, 10):
        if i % j == 0:
            arr [j -  2] += 1

dict={}
x = 0
while x < len(arr):
        dict[x + 2] = arr[x]
        x += 1

for key in dict:
    print(key, ' - ', dict[key])
