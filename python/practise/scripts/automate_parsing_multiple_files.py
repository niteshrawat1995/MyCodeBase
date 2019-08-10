'''Trying to automate a task which require to sort no. of files(folders) based on thier correct order!'''

import os

os.chdir('/home/niteshrawat/Documents/')
print(os.getcwd())

# help(os.listdir(path))

for files in os.listdir(os.getcwd()):
    # storing the filename and ext in seperate variables
    file_name, file_extn = os.path.splitext(files)

    file_text, file_order = file_name.split('-')
    #stripping the extra whitespaces and making the order nums in 2 digits.Also removing the # symbol!
    file_order = file_order.strip()[1:].zfill(2)

    # Reformatting the file name based on our requirement.
    print('{}-{}'.format(file_order, file_text))
    new_name = '{}-{}'.format(file_order, file_text)

    # assigning the new name to the file currently in for loop.
    os.rename(files, new_name)
