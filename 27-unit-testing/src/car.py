class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def show(self):
        print(f"{self.color} car, speed = {self.speed}")

    def is_faster_than(self, other_car):
        return True if self.speed > other_car.speed else False


hello = 10
