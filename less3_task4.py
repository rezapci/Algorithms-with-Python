# Determine which number in the array is most common.

import random

arr = [random.randint(1, 50) for _ in range(35)]

print(arr)

n = arr[0]
n_quantity = 1

for i in range(len(arr)):
    quantity = 1
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            quantity += 1
    if quantity > n_quantity:
        n_quantity = quantity
        n = arr[i]


print ('The number {} is most common. The number of repetitions is - {}'.format(n, n_quantity))
