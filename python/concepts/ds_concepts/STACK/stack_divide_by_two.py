'''
Use a stack data structure to convert interger values to binary.
Hint: Remainders of division of integer by 2 will produce its binary representation *up side down*.
for ex:
242 /2 = 121 -> 0(242%2)
121 /2 = 60  -> 1(121%2)
...            ...
1/2 = 0      -> 1(1%2)
'''
from Stack import Stack


def int_to_bin(num):
    s = Stack()
    binary_rep = []
    while num > 0:
        s.push(num % 2)
        num = num // 2
    while not s.is_empty():
        binary_rep.append(s.pop())
    return ''.join(map(str, binary_rep))

# Driver/Test
print(int_to_bin(242))
