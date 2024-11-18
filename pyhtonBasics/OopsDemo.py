# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructor etc
# objects for your classes

#self keyword is mandatory for calling variable name into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you creat object

class Calculator:

    num = 100 # class variables
    # default constructor

    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())