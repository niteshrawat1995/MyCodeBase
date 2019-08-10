'''Binary search requires the data to be sorted.
Time Complexity = 0(nlogn)(<0(n))
Space Complexity = 0(1) since no external ds is used.(Inplace)
'''


def binary_search_iterative(seq, val):
    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = (low + high) // 2
        if val == seq[mid]:
            return True

        elif val < seq[mid]:
            high = mid - 1

        else:
            low = mid + 1
    return False


def binary_search_recursive(seq, val, low, high):
    # Base condition
    # If the value of low after recursion calls get greater than high or value of high get lesser than low, means that the value is not present on the sequence.
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if val == seq[mid]:
            return True
        elif val < seq[mid]:
            return binary_search_recursive(seq, val, low, mid - 1)
        else:
            return binary_search_recursive(seq, val, mid + 1, high)

# Driver


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(binary_search_iterative(A, 4))
print(binary_search_recursive(A, 4, 0, len(A) - 1))
