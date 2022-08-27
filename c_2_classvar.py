class Employee:

    # class variable
    noOfEmp = 0
    rasieAmt = 1.04

    def __init__(self, fName: str = 'first', lName: str = 'last', pay: int = 0) -> None:
        # instance variable
        self.fName = fName
        self.lName = lName
        self.pay = pay
        self.email = f'{fName}.{lName}@company.com'
        Employee.noOfEmp += 1

    def fullname(self) -> str:
        return f'{self.fName} {self.lName}'

    def apply_raise(self):
        self.pay = int(self.pay * self.rasieAmt)


print(f"noOfEmp = {Employee.noOfEmp}")
emp_1 = Employee('Dishant', 'Raut', 5000)  # instance variable
emp_2 = Employee('Ankita', 'Harad', 9000)  # instance variable
print(f"noOfEmp = {Employee.noOfEmp}")

# 1
# print(f"classVar Class Access = {Employee.rasieAmt}")
# print(f"classVar Instance Access = {emp_1.rasieAmt}")
# print(f"classVar = {Employee.__dict__}")

# 2
# Employee.rasieAmt = 1.05
# print(f"classVar Instance Access = {emp_1.rasieAmt}")

# 3
# emp_2.rasieAmt = 1.02
# print(f"classVar Class Access = {Employee.rasieAmt}")
# print(f"emp_1.rasieAmt = {emp_1.rasieAmt}")
# print(f"emp_1.__dict__ = {emp_1.__dict__}")
# print(f"emp_2.rasieAmt = {emp_2.rasieAmt}")
