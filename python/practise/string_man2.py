"""
Write a program to get a string S, type of conversion 1- lowercase 2- uppercase, T and integer P. Convert the case of the letters in the positions which are multiples of P.
input:
ProFiLe
1
2
output:
proFiLe
"""


def func(seq, case_type, p):
    if len(seq) == 0:
        return "String cannot be empty."
    else:
        n = len(seq)
        for i in range(n):
            if (i % p == 0):
                if case_type == 1:
                    seq = seq[:i] + seq[i].lower() + seq[i + 1:]
                else:
                    seq = seq[:i] + seq[i].upper() + seq[i + 1:]
        return(seq)


print(func("ProFILe", 1, 2))
