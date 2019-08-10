# getters,setters and deleters can be implemented in python using property decorators.
# property decorators allows us to define a mehtod which we can access as an attribute.
# @property is the pythonic way of creating getter and setter.


class Employee(object):

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # getter-like
    @property
    def email(self):
        print('getting email')
        return '{}.{}@company.com'.format(self.first, self.last)

    # getter-like
    @property
    def fullname(self):
        print('getting fullname')
        return '{} {}'.format(self.first, self.last)

    # setter-like
    @fullname.setter
    def fullname(self, name):
        print('setting fullname')
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # deleter-like
    @fullname.deleter
    def fullname(self):
        prin('deleting fullname')
        self.first = None
        self.last = None
        print('Delete name!')


emp1 = Employee('Nitesh', 'Rawat', '20000')
# we now cannot set the attribute like this:
#emp1.email = 'Nitesh.chopra@gmail.com'
# To do the above task we need a setter


print(emp1.fullname)
# print(emp1.email)
emp1.fullname = 'Time Tom'
print(emp1.fullname)
