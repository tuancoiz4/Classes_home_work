class Vehicle:
    def __init__(self,make,model,year,weight,Trips,NeedMaintenance = False):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedMaintenance = NeedMaintenance
        self.trips = Trips
# Vehicle1 = Vehicle("Honda","Civic","2001",2,False,99)
# print(Vehicle1.trips)
class Cars(Vehicle):
    def __init__(self,make, model,year,weight,Trips,NeedMaintenance = False,isDriving = False):
        Vehicle.__init__(self,make,model,year,weight,NeedMaintenance,Trips)
        self.isDriving = isDriving
    # gettings
    def getManufactors(self):
        return ("This car is made by: " + self.make +"\nThe model is: "+ self.model\
            + "\nYear of manufacturing is: "+ str(self.year) + "\nThe weight is: "+str(self.weight) +"tons")
    
    def getStatus(self):
        if self.NeedMaintenance == False:
            return ("Trips since last maintenance: " +str(self.trips) + "\nMaintenanace is not needed!")
        else: 
            return ("Trips since last maintenance: " +str(self.trips) + "\nMaintenanace is needed!")
    # methods
    def driving(self):
        self.isDriving = True
        self.trips = self.trips + 1
        if self.trips >= 100:
            self.NeedMaintenance = True
    def stop(self):
        self.isDriving = False
    def repair(self):
        if self.NeedMaintenance == True:
            self.trips = 0
            self.NeedMaintenance = False
        else:
            return ("This car doesn't need to repair!")
class Plane(Vehicle):
    def __init__(self,make, model, year, weight,Trips,NeedMaintenance = False, isFlying = False):
        Vehicle.__init__(self,make,model,year,weight,NeedMaintenance,Trips)
        self.isFlying = isFlying
    # getting
    def getManufactors(self):
        return ("This plane is made by: " + self.make +"\nThe model is: "+ self.model\
            + "\nYear of manufacturing is: "+ str(self.year) + "\nThe weight is: "+str(self.weight) +"tons")
    def getStatus(self):
        if self.NeedMaintenance == True:
            return ("Trips since last maintenance is: "+str(self.trips)+" Maintenance is needed")
        else:
            return ("Trips since last maintenance is: "+str(self.trips)+" Maintenance is not needed")
    def Flying(self):
        if self.NeedMaintenance == True:
            return ("This plane cannot fly until it's repaired")
        else:
            self.isFlying = True
            self.trips = self.trips +1
            if self.trips >= 100:
                self.NeedMaintenance = True
    def Landing(self):
        self.isFlying = False
    def repair(self):
        if self.NeedMaintenance == True:
            self.trips = 0
            self.NeedMaintenance = False
        else:
            return ("this plane doesnt need repair!")
# #Car1
# car1 = Cars("Honda","Civic",2020,2,False,99,False)
# print(car1.getManufactors())
# print(car1.getStatus())
# car1.driving()
# print(car1.getStatus())
# car1.driving()
# print(car1.getStatus())
# car1.repair()
# print(car1.getStatus())
#plane1
plane1 = Plane("Boeing","777",2014,20,False,99,False)
print(plane1.getManufactors())
print(plane1.getStatus())
plane1.Flying()
print(plane1.getStatus())
print(plane1.Flying())
