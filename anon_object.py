#This is mocking the C# ability to do anonymous objects on the fly
#this requires a quick class that inherits dict (due to anon objects only having
#properties and fields you just have to define get and set methods of properies in the AnonObject Class
#you see below

class AnonObject(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__ 


#Once class is created this is how to create an anonymous object
SomeAnonObject = AnonObject(id = 7, registered = True, name = "Matt")

#and print it
print(SomeAnonObject)