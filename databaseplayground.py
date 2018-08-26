from pony.orm import *

db = Database()

class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')

class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)

show(Person)
