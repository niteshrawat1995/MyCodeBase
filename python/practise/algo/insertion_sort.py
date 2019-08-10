# Insertion sort
# Compare the element at position after the till_sorted slice
# If strictly lesser than last element of the till_sorted slice than swap.
# Repeat till the first element of the slice, now the till_sorted slice increased by 1.


class Insertion:
    def __init__(self, sequence):
        self.sequence = sequence

    @staticmethod
    def insertion_sort(seq):
        for i in range(len(seq) - 1):
            for j in range(i + 1, 0, -1):
                if seq[j] < seq[j - 1]:
                    seq[j], seq[j - 1] = seq[j - 1], seq[j]
        return seq


print(Insertion.insertion_sort([9, 7, 8, 5, 6, 4, 2, 1]))
#a= [9,7,8,5,6,4,2,1]
# print(insertion_sort(a))
