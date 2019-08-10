'''Copying context of a file(photo) to another file(new) using python!'''

'''rb --> read binary & wb --> write binary. These operations are required for a photo file.'''
with open('/home/niteshrawat/Downloads/my_pic.jpg', 'rb') as rf:
    with open('copy_my_pic.jpg', 'wb') as wf:
        # reading all lines from rf
        for line in rf:
            # writinf those lines in wf
            wf.write(line)
