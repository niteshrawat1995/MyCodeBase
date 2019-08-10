"""
my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)

This should have the following output:
This
is
a
test
"""

class Sentence(object):

    def __init__(self, seq):
        self.seq = seq
        self.index = 0
        self.words = self.seq.split()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current = self.words[self.index]
        except:
            raise StopIteration
        else:
            self.index +=1
            return current
        
