from Vehicle import Vehicle

class Floor():
    def __init__(self,max_rows=5,max_slot_per_row=20,levels = 4) :
        self.rows = max_rows
        self.max_slot_per_row = max_slot_per_row
        self.vehicles = [Vehicle]
        self.max_levels = levels

    def park_vehicle(self,vehicle:Vehicle):
        if self.Find_slot()>= vehicle.vehicle_size:
            print("There are slots available")
            self.vehicles.append(vehicle) 
        elif self.Find_slot()< vehicle.vehicle_size:   
            return False
        print("There are no Slots available")

    def remove_vehicle(self,vehicle:Vehicle):
        self.vehicles.remove(vehicle)
        print("Vehicle removed")
    

    def Find_slot(self):
        #check first for free slot in one row
        avlSlots = self.max_slot_per_row
        for v in self.vehicles :
            avlSlots = self.max_slot_per_row - v.vehicle_size
            return avlSlots

    def Find_slot_to_next_row(self,vehicle:Vehicle):   
         for r  in range(6) :
             if self.Find_slot()>= vehicle.vehicle_size:
                print("There are slots available")
                self.vehicles.append(vehicle) 
             elif self.Find_slot()< vehicle.vehicle_size:   
                return False
             print("There are no Slots available")
    