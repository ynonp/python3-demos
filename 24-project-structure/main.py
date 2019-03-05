import src.car as car
# import car as cc

from src.race import Race

c1 = car.Car('blue', 40)
c2 = car.Car('green', 60)
race = Race([c1, c2])

c1.show()

print(car.hello)

race.winner().show()
