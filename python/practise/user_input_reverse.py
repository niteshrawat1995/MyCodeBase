
sentence = "intAllStudents = { x : intAllStudents . count ( x ) for x in intAllStudents NameError : name ' intAllStudents ' is not defined "
sentence = [str(i) for i in sentence.split()]

sentence = {i:sentence.count(i) for i in sentence}
print(sentence)
