# Inheritance and Polymorphism in Python 


#Person is a Base/Parent class
class Person:
    def __init__(self, name):
        self.name = name
    
    def job(self):
        pass


#Teacher and Student are child class
class Teacher(Person):
    def job(self):
        print('My name is: ', self.name, 'I am a Teacher')

class Student(Person):
    def job(self):
        print('My name is', self.name, 'I am Student')



# we can see the job function use in multiple class and give output multiple value
# this method called polimarphysm
# this is also called method overriding
#same method, same parameter in use method overriding

#method overloading means same function use in same class with different parameter name
#this is not possible in python3


person1 = Teacher('Aynul')
person1.job()

person2 = Student('Avee')
person2.job()

# we can not access to the private method
# __ use for private method declaring



# we access private data by using _className__methodName(),so that
# its called data hiding  and encapsulation

class Employee():
    def __password(self):
        print('private employee')

    

privateEmployee = Employee()
privateEmployee._Employee__password()


#If you want to access and change the private variables, accessor (getter) methods and 
# mutators(setter methods) should be used, as they are part of Class. 


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def display(self):
        print(self.name)
        print(self.__age)
 
    def getAge(self):
        print(self.__age)
 
    def setAge(self, age):
        self.__age = age
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#changing age using setter
person.setAge(35)
person.getAge()




#1) What is Abstraction in Python?

#Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on how to use the application.
#An abstract class can have both a normal method and an abstract method

#2) How can we achieve Abstraction in Python?

#In Python, abstraction can be achieved using abstract classes and methods.


#3) Whether an abstract class can be instantiated?

#No, the abstract class cannot be instantiated, i.e., we cannot create objects for the abstract class.


#4) Mention the name of the module to be imported for an abstract class

#‘abc’ is the module to be imported when we define an abstract class in Python programs. ‘abc’ stands for ‘abstract base class’.