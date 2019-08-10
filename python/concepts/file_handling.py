# File Handling using python:

# 1. READING FILE :

with open('/home/niteshrawat/python/practise/alcohol.txt', 'r') as f:
    print(f.name)
    size_to_read = 100
    f_contents = f.read()  # read(size_to_read) --> size is the no. of character to read.
    print(f_contents)

# file gets automatically closed when we use 'with open'.
print(f.closed)  # True
# file can be referenced even after closing. But no new operations can be performed.
# print(f_contents)

# 2. WRITING FILE :

# if the file is not present, a new file will be created(alcohol2). If the file is present then it overwrites it.
with open('/home/niteshrawat/python/practise/alcohol2.txt', 'w') as f2:  # open('file_path',a) --> append the file
    #f2.write('Hello!')
    f2.write('Hi!')
