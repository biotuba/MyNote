# OO 物件

class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def bmi(self):
        return self.weight / (self.height/100)**2

    def is_overweight(self):
        if self.bmi() >= 30:
            print('過重')
        else:
            print('正常')
    

p1 = Person('Jay', 93, 173)
print(p1.bmi())
p1.is_overweight()
