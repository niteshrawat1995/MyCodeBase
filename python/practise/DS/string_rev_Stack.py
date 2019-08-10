# Reversing a string using stack

def rev_str(seq):
    seq = list(seq)
    rev = []
    for i in range(len(seq)):
        rev.append(seq.pop())
    return ''.join(rev)

print(rev_str('Nitesh'))
