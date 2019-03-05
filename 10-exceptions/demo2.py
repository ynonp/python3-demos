def raise_unless_divides_by_3(num):
    if num % 3 != 0:
        raise Exception("Hahaha")


try:
    raise_unless_divides_by_3(2)
except Exception:
    print("Sorry exception")