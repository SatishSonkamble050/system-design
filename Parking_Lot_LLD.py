import uuid
from datetime import datetime,timezone
import math
class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.id = str(uuid.uuid4())
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

class Ticket:
    def __init__(self, vehicle_number, spot_id):
        self.id = str(uuid.uuid4())
        self.spot_id = spot_id
        self.vehicle_number = vehicle_number
        self.entry_time = datetime.now(timezone.utc)
        self.exit_time = None
        self.amount = 0

    def close_ticket(self):
        self.exit_time = datetime.now(timezone.utc)

    def calculate_amount(self):
        duration = self.exit_time - self.entry_time        
        hours = duration.total_seconds()/3600
        billable_hours = math.ceil(hours)
        self.amount = round(billable_hours * 20,2)
        print(f"DURATION : {duration} --- HOURS : {hours} --- AMOUNT : {self.amount}")
        return self.amount
    
class ParkingSpot:
    def __init__(self, spot_id, vehicle_type):
        self.id = spot_id
        self.vehicle_type = vehicle_type
        self.is_free = True
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_free = False
    
    def remove_vehicle(self):
        self.vehicle = None
        self.is_free = True


class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)
    
    def remove_spot(self, spot_id):
        self.spots = [s for s in self.spots if s.id != spot_id]


    def find_free_spot(self, vehicle_type):
        print("finf.... :", vehicle_type)
        for spot in self.spots:
            if spot.vehicle_type == vehicle_type  and spot.is_free == True:
                return spot

        return None


class Parking_Lot:
    def __init__(self):
        # self.lot_number = lot_number
        self.floors = []
        self.tickets = {}

    def add_floor(self, floor):
        self.floors.append(floor)
    
    def entry_vehicle(self, vehicle):
        print("VEChicle : ", vehicle.vehicle_type)
        print("FLOOR  : ", self.floors)
        for floor in self.floors:
            print("ENTRY : ", floor)
            spot = floor.find_free_spot(vehicle.vehicle_type)
            print("SPOT IN : ", spot)
            if spot:
                spot.assign_vehicle(vehicle)
                ticket = Ticket(vehicle, spot_id=spot.id)

                self.tickets[ticket.id]  ={
                    "ticket" : ticket,
                    "spot" : spot
                }

                return ticket        
        
        return None
    

    def exit_vehicle(self, ticket_id):
        if ticket_id not in self.tickets:
            return None
        
        data = self.tickets[ticket_id]

        ticket = data["ticket"]
        spot = data["spot"]

        ticket.close_ticket()
        amount = ticket.calculate_amount()
        spot.remove_vehicle()

        return amount
    


plot1 = Parking_Lot()

floor1 = ParkingFloor(123)
spot1 = ParkingSpot(1, "car")
spot2 = ParkingSpot(2, "car")

floor1.add_spot(spot1)
floor1.add_spot(spot2)

plot1.add_floor(floor=floor1)

v1 = Vehicle(1425, "car")

ticket = plot1.entry_vehicle(v1)


print("LOT : ", ticket.id)

amount = plot1.exit_vehicle(ticket_id=ticket.id)
print("AMOUNT :", amount)

print("FLOOR : ", floor1.spots)






        
