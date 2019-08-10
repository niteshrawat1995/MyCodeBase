class Employee(object):
    num_of_emp = 0
    raise_amount = 1.4

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emp += 1

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        cls.first = first
        cls.last = last
        cls.pay = pay
        return cls(first, last, pay)

    def apply_raise(self):
        self.pay = self.pay * Employee.raise_amount

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def status(self):
        return 'In a relationship & Angry!'

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):

    raise_amount = 1.7

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

    @property
    def status(self):
        return 'Single & Happy!'


class Manager(Employee):
    """docstring for Manager"""

    def __init__(self, first, last, pay, employees=[]):
        super(Manager, self).__init__(first, last, pay)
        self.employees = employees

    def add(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def manages(self):
        for emp in self.employees:
            print(emp.email)

    @property
    def status(self):
        return 'Married & Sad!'


emp1 = Employee('John', 'Wick', 1000)
print(type(emp1))
print(emp1.email)
emp2 = Employee.from_string('John-Rambo-2000')
print(type(emp2))
print(emp2.email)

print('Total number of employees = ', Employee.num_of_emp)
# above st proves that class obj calls the __init__() of the class.
import datetime
my_date = datetime.date(2018, 5, 27)
print(Employee.is_workday(my_date))


dev1 = Developer('Dennis', 'Richie', 30000, 'C')
print(dev1.email)
print(dev1.prog_lang)

mgr1 = Manager('Bill', 'Gates', 50000)
print(mgr1.fullname)

mgr1.add(dev1)
mgr1.manages()

print("Employee's life:", emp1.status)
print("Developer's life:", dev1.status)
print("Manager's life:", mgr1.status)

print('Dev raise amount', dev1.raise_amount)
print('Employee raise amount', emp1.raise_amount)

dev1.apply_raise()
print(dev1.pay)
