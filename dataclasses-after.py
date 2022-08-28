# * https://www.youtube.com/watch?v=vRVVyl9uaZc

from dataclasses import dataclass, field, asdict, astuple


@dataclass(order=True, frozen=True)
class Person:
    # instance variable
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # runs after constructor
        # self.sort_index = self.strength # use when [frozen = False]
        object.__setattr__(self, 'sort_index', self.strength) # use when [frozen = True]

    def __str__(self):
        # a better string represntation
        return f'{self.name}, {self.job} ({self.age})'


person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(person1)
print(asdict(person2))
print(astuple(person2))
print(id(person2))
print(id(person3))
print(person3 == person2) # works [order = True] & sort_index is required
print(person1 > person2)
