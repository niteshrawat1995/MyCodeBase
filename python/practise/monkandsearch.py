def not_less(seq, num):
    result = [x for x in seq if x > num]
    return len(result)


def not_greater(seq, num):
    result = [x for x in seq if x < num]
    return len(result)


n = int(input())

seq = [int(x) for x in input().split(' ')]

m = int(input())

for case in range(m):
    var, value = input().split(' ')
    var, value = int(var), int(value)
    if var == 0:
        print(not_less(seq, value))
    else:
        print(not_greater(seq, value))
