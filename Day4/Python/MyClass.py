#!/usr/bin/python

class MyClass:

     def __init__(self):
         print ("Thats is called as constructor")
         print ("You can initialize member variable here automatically")
         self.x = 100
         self.y = 200

     def setValues(self, val1, val2):
         self.x = val1
         self.y = val2

     def printValues(self):
         print ("Value of x is ", self.x)
         print ("Value of y is ", self.y)
         print ("\n")

if __name__ == "__main__":
  print("Constructing Object 1")
  obj1 = MyClass()
  print("Constructing Object 2")
  obj2 = MyClass()

  print("Before calling setValues function,Object 1 values ")
  obj1.printValues()

  print("Before caling setValues function,Object 2 values ")
  obj2.printValues()

  obj1.setValues(400,500)
  obj2.setValues(10,20)

  print("After calling setValues function")
  print("Object 1 values")
  obj1.printValues()
  print("Object 2 values")
  obj2.printValues()

