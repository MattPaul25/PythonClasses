
#all variables are first class objects 

def main():
    print("starting")


class Car(object):
    def __init__(self, carName):
        Car.name = carName
        Car.Park = True
        Car.On = False
        Car.speed = 0
        print("your new car is a {0}.".format(Car.name))

    def turn_on(self):
        if (not Car.On):
            Car.On = True;
            print("vroom, vroom")
        else:
            print("Car is already on")

    def turn_off(self):        
        if (Car.On and Car.speed == 0):
            Car.On = False;
            print("perperperpderp")
        elif not Car.On:
            print("Car is already off")
        elif(Car.speed > 0):
            print("can't turn off: Car is moving")

    def accelerate(self, amount = 1):
        if Car.On:
            Car.speed += amount
            status = " speeding up: {0} is going {1} mph faster: current speed {2} ".format(Car.name, amount,  Car.speed)
            print(status)
        elif not Car.On:
            status = "cant speed up: car is off"
            print(status)

    def decelerate(self, amount = 1):
         if Car.On:
            Car.speed -= amount
            status = " slowing down: {0} is going {1} mph slower: current speed {2} ".format( Car.name, amount, Car.speed)
            print(status)
         elif not Car.On:
            status = "cant slow down: car is off"
            print(status)

    def HandBreak(self):
        Car.Speed -= Car.speed
        Car.Park = True


main()
C = Car("ferrari")
C.turn_on()
C.accelerate(56)
C.decelerate(20)
C.turn_off()