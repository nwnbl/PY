from car_p150 import Car

my_car=Car('audi', 'a8l', '2021')

my_car.update_odometer(20)

print(my_car.get_descriptive_name())

my_car.read_odometer()