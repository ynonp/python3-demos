class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point [{self.x}, {self.y}]"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.x) & hash(self.y)


p1 = Point(10, 10)
p2 = Point(10, 10)
p3 = Point(10, 15)

print(p1 == p2)

s = set()
s.add(p1)
s.add(p2)
print(len(s))
