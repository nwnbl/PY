class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Mileage cannot roll back!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def read_odometer(self):
        print(f"This Electrical car has {self.odometer_reading} miles on it.")

#my_tesla = ElectricCar('tesla', 'model s', '2019')
#print(my_tesla.get_descriptive_name())  
#my_tesla.update_odometer(10)
#my_tesla.read_odometer()

