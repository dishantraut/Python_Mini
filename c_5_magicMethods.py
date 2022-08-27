class Employee:

    rasieAmt = 1.04

    def __init__(self, fName: str = 'first', lName: str = 'last', pay: int = 0) -> None:
        self.fName = fName
        self.lName = lName
        self.pay = pay
        self.email = f'{fName}.{lName}@company.com'

    def fullname(self) -> str:
        return f'{self.fName} {self.lName}'

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.rasieAmt)

    def __repr__(self) -> str:
        return f"Employee('{self.fName}', '{self.lName}', {self.pay})"

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other: int = 0) -> int:
        return f"{self.pay + other.pay}"

    def __len__(self) -> int:
        return f"{len(self.fullname())}"


emp_1 = Employee('Dishant', 'Raut', 5000)
emp_2 = Employee('Pritam', 'Kokitkar', 9000)
print(f"repr/str : {emp_1}\n")
print(f"repr = {repr(emp_2)}")
print(f"str = {str(emp_2)}\n")
print(f"__repr__ = {emp_2.__repr__()}")
print(f"__str__ = {emp_2.__str__()}\n")
print(f"__add__ = {emp_2+emp_1}\n")
print(f"__len__ = {emp_1.__len__()}\n")
