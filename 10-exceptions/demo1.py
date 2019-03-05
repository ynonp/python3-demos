def sum_of_digits(n):
    result = 0
    while n > 0:
        digit = n % 10
        n //= 10
        result += digit

    return result


def read_until_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


x = read_until_number("select number:")
res = sum_of_digits(x)
print(f"sum of digits of {x} is {res}")

