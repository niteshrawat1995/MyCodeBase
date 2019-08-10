import re

with open('alcohol.txt', 'r') as f:
    print(f.name)
    f_content = f.read()

# print(f_content)

pattern = re.compile(r'[A,a]lcohol')
matches = pattern.finditer(f_content)

for match in matches:
    print(str(match.group()) + '-->' + str(match.span()))
