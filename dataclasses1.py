class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    # * Modify the default representaion of the object. eg:- <__main__.Person object at 0x000001D1A8B95FD0>
    # * Main File - Person Class - at Memory Location
    # def __repr__(self) -> str:
    #     return (f"Person ({self.name}, {self.age}, {self.city})")

    # * Modify the equality check of the object. eg:- will always return False
    # def __eq__(self, o: object) -> bool:
    #     return (self.name, self.age, self.city) == (o.name, o.age, o.city)

p = Person("Dishant", 33, "BH")
q = Person("Dishant", 33, "BH")
print(p)
print(q)
print(p == q)


from dataclasses import dataclass

@dataclass
class NewPerson:
    name: str
    age: int
    city: str

p1 = NewPerson("Dishant", 32, "FORT")
q1 = NewPerson("Dishant", 32, "FORT")
print(p1)
print(q1)
print(p1.name, p1.age, p1.city)
print(q1.name, q1.age, q1.city)
print(p1 == q1)
