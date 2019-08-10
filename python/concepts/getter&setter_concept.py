'''Getters and setters are used to make the data available only through methods.
   This prevents user to manually change the values any time.'''

class Customer(object):

    def __init__(self, name, savings):
        self.set_Name(name)
        self.set_Savings(savings)

    # setters for name,savings ::
    def set_Name(self, value):
        self._name = value

    def set_Savings(self, value):
        self._savings = value

    # getters for name,savings ::
    def get_Name(self):
        return self._name

    def get_Savings(self):
        return self._savings


tim = Customer('NITESH', 1000)

tim.set_Name('TIM')
print(tim.get_Name())
