class Student:
    grade = 10
    name = "Penguin"
    
    def intro(self):
        print("Hi im student at idk school")
        
    def details(self):
        print("My name is "+str(self.name))
        print("I study in Grade "+str(self.grade))
        
ob = Student()
ob.intro()
ob.details()
class Parrot:
    # class attribute
    species = "bird"
    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self,large):
        print("hello",large)
# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
print(blu.display(10))