"""
Define and lookup items in dictionaries
"""

shapes = {
    'triangle': 3,
    'rectanble': 4
}

print(shapes['triangle'])

shapes['square'] = 4
print(shapes)

del(shapes['triangle'])
print(shapes)

print(len(shapes))

if 'triangle' in shapes:
    print('triangle is a valid key in shapes')

try:
    print(shapes['rectangle'])
except KeyError:
    print("rectangle is not a valid key")