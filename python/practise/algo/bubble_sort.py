# Bubble sort: Compares the adjacent elements in a way that the larger element bubbles to the right.
# After each iteration the largest element bubbles to the righmost position of the array.
# It runs in O(n**2)

print('Bubble Sort Algorithm :\n')
print('Unsorted list.')
num = [5, 8, 1, 6, 9, 2]
print(num)

for i in range(0, len(num)):
    for j in range(0, len(num) - 1 - i):  # As the last element is already sorted, we want to iterate till 2 positons before the sorted elements.
        if num[j] > num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp
print('Sorted list.')
print(num)
