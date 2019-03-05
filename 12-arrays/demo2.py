grades = [99, 80, 70, 55, 90]
fruits = ['apple', 'banana', 'lemon']

high_grades_only = [g for g in grades if g > 80]
lengths = [len(t) for t in fruits]

print(lengths)
