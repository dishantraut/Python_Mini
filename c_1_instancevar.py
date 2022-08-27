# Reference :-
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=1

class Employee:
    def __init__(self, fName: str = 'first', lName: str = 'last', pay: int = 0) -> None:
        # instance variable
        self.fName = fName
        self.lName = lName
        self.pay = pay
        self.email = f'{fName}.{lName}@company.com'

    def fullname(self) -> str:
        return f'{self.fName} {self.lName}'


emp_1 = Employee('Dishant', 'Raut', 5000)  # instance variable
emp_2 = Employee('Ankita', 'Harad', 9000)  # instance variable
emp_3 = Employee()

print(f"self passed automatically = {emp_1.fullname()}")
print(f"self passed manually = {Employee.fullname(emp_1)}")
print(f"emp_3 = {emp_3.fullname()}")
print(f"annotations = {emp_3.__init__.__annotations__}")
