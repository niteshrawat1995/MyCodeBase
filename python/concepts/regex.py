# findall() returns a list of matched value
# finditer() returns the match objects.


import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
pattern = re.compile(r'\d{3}.\d{3}.\d{3,4}')

# using the finditer()
matches = pattern.finditer(text_to_search)

for match in matches:
    print(str(match.group()) + '-->' + str(match.span()))

# using findall()
#matches = pattern.findall(text_to_search)
# print(matches)
