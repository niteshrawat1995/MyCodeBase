class Employee(object):

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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees == None:
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
        for name in self.employees:
            print('--->', name.full_name())


dev_1 = Developer('Nitesh', 'Rawat', 20000, 'Python')
print(dev_1.prog_lang)
dev_2 = Developer('Navpreet', 'Singh', 35000, 'Swift')

mgr_1 = Manager('Jushal', 'Tewari', 90000, [dev_1, dev_2])

print(mgr_1.email)
mgr_1.print_emps()

mgr_1.remove_emp(dev_2)
mgr_1.print_emps()
