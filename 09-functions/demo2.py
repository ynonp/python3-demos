def sum_of_digits(n):
    result = 0
    while n > 0:
        digit = n % 10
        n //= 10
        result += digit

    print(result)

sum_of_digits(651)
