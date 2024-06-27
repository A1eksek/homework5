class Homer:
    def __init__(self, name):
        self.name = name

class Daughter(Homer):
    pass

daughter1 = Daughter('Lisa')
print(daughter1.name)

####################################

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    pass

class Circle(Shape):
    pass

class Triangle(Shape):
    pass

#########################################

class Animal:
    def make_sound(self):
        print('')

class Dog(Animal):
    def make_sound(self):
        print('гав')

class Cat(Animal):
    def make_sound(self):
        print('мяу')

class Bird(Animal):
    def make_sound(self):
        print('чик-чирик')

dog = Dog()
cat = Cat()
bird = Bird()

dog.make_sound()
cat.make_sound()
bird.make_sound()


