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
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(str(match.group()) + '-->' + str(match.span()))
    # print(match.span())
