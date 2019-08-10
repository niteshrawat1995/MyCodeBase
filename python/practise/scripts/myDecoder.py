def getValues(digits, n):
    result = ''
    if n == 1:

        for digit in digits:
            if int(digit) == 1:
                result += 'A'
            elif int(digit) == 2:
                result += 'B'
            elif int(digit) == 3:
                result += 'C'

    else:
        for i in range(len(digits) - 1):
            if int(digits[i:i + 2]) == 11:
                result += 'K'
                break
            elif int(digits[i:i + 2]) == 12:
                result += 'L'
                break
            elif int(digits[i:i + 2]) == 21:
                result += 'V'
                break
    return result


def decoder(digits):

    count = 0
    n = len(digits)
    print(getValues(digits, 1))

    for i in range(len(digits) - 1):
        value = int(digits[i:i + 2])
        if value >= 0 and value < 27:
            print(getValues(digits[:i], 1) + getValues(digits[i: i + 2], 2) + getValues(digits[i + 2:n], 1))
            count += 1

    print('The number of encodings = ', count)


# RUN:
num = '1211'
print(decoder(num))
