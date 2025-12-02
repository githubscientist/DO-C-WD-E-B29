'''
Class:
    - class is a blueprint or template for creating objects. 
    - It defines attributes (data) and methods (functions) that the created objects will have.
    - It is also called as collection of objects.

Object:
    - An object is an instance of a class.

Data Encapsulation:
    - Data encapsulation is the concept of wrapping data (attributes) and methods (functions)
        together within a single unit, i.e., class.

Data Abstraction:
    - Data abstraction is the concept of hiding the internal details and showing only the essential features of
        an object.
    
Inheritance:
    - Inheritance is a mechanism where a new class (child class) can inherit attributes and methods from an existing    
        class (parent class).

Polymorphism:
    - Method Overriding is a way to achieve polymorphism in Python OOP.
    - It allows a child class to provide a specific implementation of a method that is already defined in its parent class.
'''

# defining a class

# Parent Class


class Student:
    '''
        attributes (data) and methods (functions)
    '''

    # This special function will be called whenever we create an object to this class
    # This special function is called as Constructor
    def __init__(self, name, yearOfBirth, course, location):
        self.name = name
        self.yearOfBirth = yearOfBirth
        self.course = course
        self.location = location

    def getAge(self):
        currentYear = 2025
        return currentYear - self.yearOfBirth

    def getFees(self):
        if self.course == 'Devops':
            return 10000
        else:
            return 5000


# Child class
class PGStudent(Student):
    def __init__(self, name, yearOfBirth, course, location):
        super().__init__(name, yearOfBirth, course, location)

    # This method overrides the parent class method getFees
    # Method Overriding
    def getFees(self):
        if self.course == 'Devops':
            return 20000
        else:
            return 10000


# create an object to the class
# s1 = Student('Krish', 2000)
# print(s1.name, 'is', s1.getAge(), 'years old')

# s2 = Student('Sathish', 2001)
# print(s2.name, 'is', s2.getAge(), 'years old')

name = input('enter the name: ')
course = input('enter the course: ')

pgs1 = PGStudent('Krish', 2000, 'Devops', 'Coimbatore')
print(pgs1.getFees())
