# Object Oriented Tutorial 1
def hello(): 
    print("Hello")

x = 1
print (type(hello))

string = "hello"
print (string.upper())

class dog:
    def __init__(self,name,age):
        self.name = name
        #print(name)
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    
    def set_age(self,age):
        self.age = age


    #def add_one(self,a):
       # return a + 1

    #def bark(self):
        #print("Bark")

d = dog("TIM", 12)
print(d.get_name(), d.get_age())
d2 = dog("Bill", 14)
print (d2.get_name(),d2.get_age())
#d.bark()
#print(d.add_one(5))
#print(type(d))