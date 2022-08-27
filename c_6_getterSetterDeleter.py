class Employee:

    rasieAmt = 1.04

    def __init__(self, fName: str = 'first', lName: str = 'last') -> None:
        self.fName = fName
        self.lName = lName

    @property
    def email(self) -> str:
        # * Getter Method
        return f'{self.fName}.{self.lName}@company.com'

    @property
    def fullname(self) -> str:
        return f'{self.fName} {self.lName}'

    @fullname.setter
    def fullname(self, name: str):
        # * Setter Method
        self.fName, self.lName = name.split(" ")

    @fullname.deleter
    def fullname(self):
        # * Setter Method
        print("Delete Name ...!")
        self.fName, self.lName = None, None


emp_1 = Employee('Dishant', 'Raut')
emp_1.fName = "John"
print(f"emp_1.first = {emp_1.fName}")
print(f"emp_1.email = {emp_1.email}")
print(f"emp_1.fullname = {emp_1.fullname}")


emp_1.fullname = "Romeo Walter"
print(f"\nemp_1.first = {emp_1.fName}")
print(f"emp_1.email = {emp_1.email}")
print(f"emp_1.fullname = {emp_1.fullname}")

del emp_1.fullname
print(f"\nemp_1.first = {emp_1.fName}")
print(f"emp_1.email = {emp_1.email}")
print(f"emp_1.fullname = {emp_1.fullname}")
