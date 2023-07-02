from Main import Car
from Acceleration_repeat import repeat
car = Car
CarLoops = repeat

Car1=car("Toyota Corolla", 2013, 0)

for _ in range(5):
    Car1.accelerate()

Car1.get_speed()

for _ in range(5):
    Car1.brake()
    Car1.get_speed()