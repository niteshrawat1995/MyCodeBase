# Class methods are methods wich take class as an argument (by using decorators).
# They can be used as alternate constructors.


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # need to always return the cls(Employee) object.
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee('Nitesh', 'Rawat', 20000)
emp_2 = Employee('Vikas', 'Sharma', 30000)

# Employee.set_raise_amount(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'Amy-Smith-70000'
#emp_str_3 = 'Angier-Santos-000'

emp_str_1 = Employee.from_string('John-Doe-70000')
# print(emp_str_1.full_name())

import datetime
my_date = datetime.date(2018, 5, 27)

print(Employee.is_workday(my_date))
