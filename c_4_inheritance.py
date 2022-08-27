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


class Developer(Employee):
    rasieAmt = 10

    def __init__(self, fName: str = 'first', lName: str = 'last', pay: int = 0, prog_lang: str = 'None') -> None:
        super().__init__(fName, lName, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, fName: str = 'first', lName: str = 'last', pay: int = 0, employees: list = None) -> None:
        super().__init__(fName, lName, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"---> {emp.fullname()}")


dev_1 = Developer('Dishant', 'Raut', 5000, 'Go Lang')
dev_2 = Developer('Pritam', 'Kokitkar', 9000, 'Python')
print(f"dev_1.email = {dev_1.email}")
print(f"dev_2.email = {dev_2.email}")
print()
# print(f"{help(Developer)}")
# print()
print(f"dev_2.pay before apply_raise = {dev_2.pay}")
dev_2.apply_raise()
print(f"dev_2.pay after apply_raise = {dev_2.pay}")
print()
print(f"dev_1.prog_lang = {dev_1.prog_lang}")
print(f"dev_2.prog_lang = {dev_2.prog_lang}")
print()
man_1 = Manager('Sakib', 'Sakharkar', 5000, [dev_1])
man_1.add_emp(dev_2)
print(f"man_1.employees = {man_1.fullname()}")
# man_1.remove_emp(dev_1)
print(f"man_1.print_emps = {man_1.print_emps()}")
print(f"isinstance = {isinstance(man_1, Manager)}")
print(f"isinstance = {isinstance(man_1, Employee)}")
print(f"isinstance = {isinstance(man_1, Developer)}")
print(f"issubclass = {issubclass(Developer, Employee)}")
print(f"issubclass = {issubclass(Employee, Developer)}")
