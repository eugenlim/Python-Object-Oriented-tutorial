# Creating of upper classes, which can get rid of using def __init__ portion

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print (f"I am{self.name} I am {self.age} years old")

class Cat(Pet):
   # def __init__(self, name, age):
   #  self.name = name
   #  self.age = age

    def speak(self):
        print ("Meow")

class Dog(Pet):
   # def __init__(self, name, age):
   #    self.name = name
   #    self.age = age

    def speak(self):
        print("Bark")

p = Pet("Marvin", 20)
p.show