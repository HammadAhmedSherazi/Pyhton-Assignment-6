# class, named car
class car:
    
    # Five Attributes
    def __init__(self, make, model, color, releaseDate, carType):
        self.make = make
        self.model = model
        self.color = color
        self.releaseDate = releaseDate
        self.carType = carType
        
    # Three methods
    def start(self, car):
        print(car + "'s Engine Started")
        
    def stop(self, car):
        print(car + "'s Engine is switched off")
        
    def autoPilot(self, car):
        print(car + " is in auto-pilot mode")

# Five object instances
carA = car("BMW", "i8", "Grey", "2014", "Sports")
print(carA.start(carA.make), carA.stop(carA.make), carA.autoPilot(carA.make))
print("Make: " + carA.make + "\nModel: " + carA.model + "\nRelease Date: " + carA.releaseDate + "\nType: " + carA.carType)

print("-------------")

carB = car("Mercedes", "S Class", "Black", "2009", "Luxury")
print(carB.start(carB.make), carB.stop(carB.make), carB.autoPilot(carB.make))
print("Make: " + carB.make + "\nModel: " + carB.model + "\nRelease Date: " + carB.releaseDate + "\nType: " + carB.carType)

print("-------------")

carC = car("Ford", "Mustang", "White & Blue", "1998", "Sports")
print(carC.start(carC.make), carC.stop(carC.make), carC.autoPilot(carC.make))
print("Make: " + carC.make + "\nModel: " + carC.model + "\nRelease Date: " + carC.releaseDate + "\nType: " + carC.carType)

print("-------------")

carD = car("Lamborghini", "Eventador", "Yellow", "2012", "Sports")
print(carD.start(carD.make), carD.stop(carD.make), carD.autoPilot(carD.make))
print("Make: " + carD.make + "\nModel: " + carD.model + "\nRelease Date: " + carD.releaseDate + "\nType: " + carD.carType)

print("-------------")

carE = car("McLaren", "P1", "Orange", "2018", "Sports")
print(carE.start(carE.make), carE.stop(carE.make), carE.autoPilot(carE.make))
print("Make: " + carE.make + "\nModel: " + carE.model + "\nRelease Date: " + carE.releaseDate + "\nType: " + carE.carType)
