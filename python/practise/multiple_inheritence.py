# In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice.


class Father(object):
    def skills(self):
        print('Father skills are: Gardening and programming.')


class Mother(object):
    def skills(self):
        print('Father skills are: Cooking and Singing.')


class Child(Father, Mother):
    pass


c = Child()
c.skills()
# Method Resolution Order (MRO) is used to find the order.
print(Child.mro())
