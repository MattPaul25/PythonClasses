#LINQ example (python version of linq)

from anon_object import AnonObject 
#importing the anonymous class from anon_object file

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{0} is {1} years old".format(self.name, self.age)

    def __repr__(self):
        return self.__str__() #now i can just print the class or a list of classes and str method is returned


people = [ 
    Person("Matt", 27),
    Person("Tony", 34),
    Person("Eric", 40),
    Person("Sarah", 30),
    Person("Sasha", 10)
    ]

people.append(Person("Alex", 23))

print(people) 

for p in people:
    print(p) #automatically prints the conversion of person into string due to override


#this is known as list comprehension
query = [ #the equivalent of a linq query 
    AnonObject(name = p.name, age = p.age) #have to use anon object as select clause
    for p in people
    if p.age >= 30  #if is the where clause
    ]

#sorted : p takes a predicate
#notice that the sorted mehtod is outside of the query expression
query = sorted(query, key = lambda p : -p.age) #-p.age is saying sort descending 


for p in query:
    print(type(p), p)