# Find the maximum negative element in the array.
# Display its value and position in the array.

import random

arr = [random.randint(-50, 50) for _ in range(10)]

print(arr)
num = -50
position = 0

for i in arr:
    if i < 0 and i > num:
        num = i


print ('The maximum negative element {}, its position: {}'.format(num, arr.index(num)))
