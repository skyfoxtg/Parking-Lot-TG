# Create a Class Vehicle 

class Vehicle():
    

# Every vehicle has attributes : licence number,vehicle size,color,model

    def __init__(self,licence_num,vehicle_size,vehicle_type) :
        self.licence_num = licence_num
        self.vehicle_size= vehicle_size
        self.vehicle_size=vehicle_size

class Car(Vehicle):
    def __init__(self, licence_num, vehicle_size, vehicle_type) :
        super().__init__(licence_num,1, vehicle_type)


class Buss(Vehicle):
    def __init__(self, licence_num, vehicle_size, vehicle_type):
        super().__init__(licence_num,5, vehicle_type)

class Truck(Vehicle):
    def __init__(self, licence_num, vehicle_size, vehicle_type):
        super().__init__(licence_num,4, vehicle_type)


class Motorcycle(Vehicle):
    pass
class ElectricCar(Vehicle):
    pass