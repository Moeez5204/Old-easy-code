class Vehicle:

    def __init__(self, name, max_speed, mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'white'
        self.capacity = capacity

    def fare(self):
        return  self.capacity *110

        
    def seating_capacity(self,capacity =50):
        return ('The capacity is ',(capacity))

class Bus(Vehicle):
    def seating_capacity(self,capacity = 50):
        return super().seating_capacity(capacity = 50)


Bigbus = Bus('Bigbus',90,20000,50)
print("Total Bus fare is:", Bigbus.fare())
print(type(Bigbus))
print(isinstance(Bigbus,Vehicle))
