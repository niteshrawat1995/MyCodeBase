# Python Object-Oriented Programming

# instance variable are variables which are unique to an instance.
# class variable are variable which are common to the all instances of the class.


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


emp_1 = Employee('Nitesh', 'Rawat', 20000)
emp_2 = Employee('Vikas', 'Sharma', 30000)

# print(emp_1.full_name())
# # This shows that the instance is actually passed as argument to the methods.
# print(Employee.full_name(emp_1))

# # raise_amount(class var) is present only class's attribute.
# print(emp_1.__dict__)
# print(Employee.__dict__)
# # but can be accessed by the instance as well.
# print(Employee.raise_amount)
# print(emp_1.raise_amount)

# # when a class var is assigned by a instance ,it becomes its attribute.
# emp_1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.__dict__)
# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(Employee.num_of_emps)
