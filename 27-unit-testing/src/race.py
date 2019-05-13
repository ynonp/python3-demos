class Race:
    def __init__(self, list_of_cars):
        self.list_of_cars = list_of_cars

    def add(self, car):
        self.list_of_cars.append(car)

    def winner(self):
        return max(self.list_of_cars, key=lambda c: c.speed)

