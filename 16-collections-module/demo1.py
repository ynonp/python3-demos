"""
Named Tuple
"""

import collections

Point = collections.namedtuple('Point', ['x', 'y'])

p1 = Point(x=10, y=20)
p2 = Point(5, 8)

print(p1)
print(p2)

print(p1.x + p2.x)
