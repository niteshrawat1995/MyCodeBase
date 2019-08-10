# Selection sort: iterates and select a min. value . Replaces this min value with the first position of the unsorted list.
# Uses nested loops.
# It runs in O(n**2)


def selection_sort(seq):
    for i in range(len(seq) - 1):
        min_val = seq[i]
        for j in range(i + 1, len(seq)):
            if min_val > seq[j]:
                min_val = seq[j]
                min_idx = j
        # swap
        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq


seq = [5, 4, 3, 2, 1]
print(selection_sort(seq))
