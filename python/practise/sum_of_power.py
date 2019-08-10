"""
1234 => (1^2)+(2^3)+(3^4)+(4^1)
"""


def sum_of_power(num):
    sum = 0
    if num < 9:
        return "Number should be greater than 9"
    else:
        num_str = str(num)
        n = len(num_str)
        first_digit = int(num_str[0])
        for i in range(n):
            if i == n - 1:
                sum += int(num_str[i]) ** first_digit
            else:
                sum += int(num_str[i]) ** int(num_str[i + 1])
    return sum


n = int(input())
print(sum_of_power(n))
