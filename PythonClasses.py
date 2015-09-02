
import Demo

def main():
    print("starting")
    C = Car("ferrari")
    C.turn_on()
    C.accelerate(56)
    C.decelerate(20)
    C.turn_off()
    C.HandBreak()
    C.turn_off()    
    print(C._name, C._Park, C._speed)


class Car(object): #everything derives from object! Class(object) implies inheritance of object but do not need it
    def __init__(self, carName):
        self._name = carName #using self is a way to make a private field that can be accessed    
        self._Park = True     # from the outside using a getter or setter internal method
        self._On = False
        self._speed = 0
        print("your new car is a {0}.".format(self._name))

    def turn_on(self):
        if (not self._On):
            self._On = True;
            print("vroom, vroom")
        else:
            print("Car is already on")

    def turn_off(self):        
        if (self._On and self._speed == 0):
            self._On = False;
            print("perperperpderp")
        elif not self._On:
            print("Car is already off")
        elif(self._speed > 0):
            print("can't turn off: Car is moving")

    def accelerate(self, amount = 1):
        if self._On:
            self._speed += amount
            status = " speeding up: {0} is going {1} mph faster: current speed {2} ".format(self._name, amount,  self._speed)
            print(status)
        elif not self._On:
            status = "cant speed up: car is off"
            print(status)

    def decelerate(self, amount = 1):
         if self._On:
            self._speed -= amount
            status = " slowing down: {0} is going {1} mph slower: current speed {2} ".format( self._name, amount, self._speed)
            print(status)
         elif not self._On:
            status = "cant slow down: car is off"
            print(status)

    def HandBreak(self):
        self._speed -= self._speed
        self._Park = True
class Test(object):
    def __init__(self, value):
        self.value = value


Demo.main()
#a = Test(123) 
a = Test('test') #a is the object that is required

#print(a.value + 2)
print(a.value.capitalize())

main()





