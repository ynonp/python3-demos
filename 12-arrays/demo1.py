x = [10, 20, 30, 'foo', 'bar', [1, 2]]
fruits = ['apple', 'banana', 'lemon']
grades = [99, 80, 70, 55, 90]

# Prints 10
print(x[0])

# Prints 90
print(grades[-1])

# Print len(x) - number of items there
# 6
print(len(x))

for index, grade in enumerate(grades):
    if grade > 80:
        print(f"{index} => {grade}")

