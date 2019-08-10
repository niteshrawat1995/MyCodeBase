# Pascal Triangle
'''
1
121
12321
1234321
'''
'''n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')

    print()
'''
# Real Pascal triangle
'''
    1
   121
  12321
 1234321
123454321
'''
'''
n = 5
for i in range(0, n):
    for j in range(n, i + 1, -1):
        print(' ', end='')

    for k in range(1, i + 1):
        print(k, end='')
    for l in range(i + 1, 0, -1):
        print(l, end='')
    print()'''
'''
Advance Pascal:
    1
    11
   121
   1331
'''

n = 5
for i in range(0, n):
    sum = 0
    for j in range(n, i + 1, -1):
        print(' ', end='')
    for k in range(1, i):
        sum += k
        print(k, end='')
        print(sum, end='')

    print()
