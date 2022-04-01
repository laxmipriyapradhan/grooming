class Flight(object):
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.passengers = [ ]
    
    def flight_summary(self):
        print(f'Flight Origin: {self.origin}')
        print(f'Flight Destination: {self.destination}')
        print(f'Flight Duration: {self.duration}')
    
    def delay(self, minutes):
        self.duration = self.duration + minutes
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    def check_in(self, passenger):
        if passenger.weight():
            self.passengers.append(passenger)
        else:
            raise ValueError("Luggage Not Allowed!!")
    
        
class Passenger:
    def __init__(self, fname, lname, passport, luggage_weight):
        self.fname = fname
        self.lname = lname
        self.passport = passport
        self.luggage_weight = luggage_weight
    
    def weight(self):
        if self.luggage_weight > 40:
            return False
        return True

p1 = Passenger("Laura", "Turner", 1234, 39)
p2 = Passenger("Bill", "Gates", 1235, 41)

f1 = Flight(origin='Bangalore', destination='Chennai', duration=60)
f2 = Flight('Bangalore', 'Delhi', 120)

f1.add_passenger(p1)
f1.add_passenger(p2)
