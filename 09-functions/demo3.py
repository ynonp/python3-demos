def sum_of_digits(n):
    """
    This function returns the sum
    of digits from its numeric argument
    """
    result = 0
    while n > 0:
        digit = n % 10
        n //= 10
        result += digit

    print(n)
    return result


x = 651
res = sum_of_digits(x)
print(f"sum of digits of {x} is {res}")
