# What is Static Method in python??
class Car:
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color
    
    def displayCarDetails(self):
        print("Car name is ",self.car_name," and Car color is ",self.car_color)

    @staticmethod
    def initialMessage():
        print("Nice Car !!!!!")

Car.initialMessage()
car1 = Car('XUV 700', 'Red')
car1.displayCarDetails()

# This will not work
# Car.displayCarDetails()

# iNeuron Company
class Employee:
    @staticmethod
    def isEmployeeOf():
        print("Employee Class for iNeuron !!")
    
Employee.isEmployeeOf()


class Calculation:
    @staticmethod
    def addTwoNums( num1, num2 ):
        print("Sum of two numbers = ", num1 + num2)
    
Calculation.addTwoNums(10,5)
