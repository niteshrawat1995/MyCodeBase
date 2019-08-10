# fixeed point is the value which is equal to the index value in which t is placed.
# Problem is to search the element and return None is no such element exist.
# Sequence is present in ascending order and distinct which makes it a suitable candidate for Binary Search.


def fixed_point(seq, low, high):
    if low > high:
        return None
    else:
        mid_idx = (low + high) // 2
        if seq[mid_idx] == mid_idx:
            return mid_idx
        elif seq[mid_idx] < mid_idx:
            return fixed_point(seq, mid_idx + 1, high)
        else:
            return fixed_point(seq, low, mid_idx + 1)


seq = [-10, -5, 0, 3, 7]
print(fixed_point(seq, 0, len(seq)- 1))
