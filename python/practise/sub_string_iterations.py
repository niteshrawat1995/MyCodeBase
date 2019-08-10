
def iterate(seq):
    iterations = []
    for passes in range(len(seq)):
        for i in range(0, len(seq) - passes):
            iterations.append(seq[i:i + passes + 1])
    return iterations


seq = 'Nitesh'
print(iterate(seq))
