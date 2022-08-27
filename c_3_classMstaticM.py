from datetime import datetime, date


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

    def __str__(self):
        # overide defualt string represntation
        return f'\nfName: {self.fName}\nlName: {self.lName}\npay: {self.pay}\nemail: {self.email}'

    def fullname(self) -> str:
        return f'{self.fName} {self.lName}'

    def apply_raise(self):
        self.pay = int(self.pay * self.rasieAmt)

    @classmethod
    def from_string(cls, emp_str: str) -> str:
        """
        Usage/Summary:
        - can be used as alternate constuctors
        - need cls as default parameter

        Args:
            emp_str (str): stirng of data with '-' as seprator

        Returns:
            str: firstName, lastName, pay
        """        
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day: datetime) -> bool:
        """
        Usage/Summary:
        - used when there is independent and logic operation needed
        - does not require any default parameter

        Args:
            day (datetime): get date using date function

        Returns:
            bool: gives false on saturday and sunday
        """        
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


# classmethod givng back data for instance variable
emp_1 = Employee.from_string('Dishant-Raut-5000')
# classmethod givng back data for instance variable
emp_2 = Employee.from_string('Ankita-Harad-9000')

print(f"emp_1 = {emp_1}")
print()
print(f"emp_2 = {emp_2.fName}")
print(f"emp_2 = {emp_2.fullname()}")
print()
print(f"Friday = {Employee.is_workday(date(2022, 8, 26))}")
print(f"Saturday = {Employee.is_workday(date(2022, 8, 27))}")
print(f"Sunday = {Employee.is_workday(date(2022, 8, 28))}")