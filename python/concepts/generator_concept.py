''' Generator is an function which yields an object which can be iterated one at a time. The function holds the previous state of the object.
Genertors is memory efficient by creating/storing an object ont at a time.'''

# genertaor can be created as function yield something(object)


def square_num(nums):
    for i in nums:
        yield (i * i)


num = square_num([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(next(a))
for squares in num:
    print(squares)

# generator can also be created using comprehension style::
cubes = (i ** 3 for i in range(11))
for cube in cubes:
    print(cube)
