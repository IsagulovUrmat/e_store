import random
import math

# list1 = random.sample(range(1,1000000),600000)

# a = list1.index(max(list1))
# b = list1.index(min(list1))
#
# if a > b:
#     x = a - b
# else:
#     x = b - a

class Human():

    def __init__(self, name, age):
        self.human_name = name
        self.age = age

    def description(self):
        print(f"{self.name} {self.age}")


class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.education = True

        def description(self):
            print(f"{self.name} {self.age} {self.education}")


class Female(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

male1 = Male(name='Steve',age=30)
male1.description()