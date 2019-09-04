# In the second array, keep the indices of even elements of the first array.
# For example, if an array is given with the values ​​8, 3, 15, 6, 4, 2,
# then in the second array you need to fill in the values ​​0, 3, 4, 5 (indexing starts from zero),
# tk exactly in these positions of the first array are even numbers.

arr_1 = [8, 3, 15, 6, 4, 2]
arr_2 = []

for i, j in enumerate(arr_1):
    if arr_1[i] % 2 == 0:
        arr_2.append(i)

print(arr_2)
