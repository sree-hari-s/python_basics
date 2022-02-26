# -*- coding: utf-8 -*-
"""Functions Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wMtvuynN6MubVzF0z6lCOOzOjIl_k6ay
"""

#Q1 and Q2
class Super:
  def fun1(self):
    print("This is function 1 in the Super class")

class Modified_Super(Super):
  def fun1(self):
    print("This is function 1 in the Modified Super class")

  def fun2(self):
     print("This is function 2 in the Modified Super class")
        
obj=Modified_Super()
obj.fun1()

#Q3
def Hello(x):
  print("This function is only having 1 argument")

def Hello(a,b):
  print("This function is having 2 arguments")

Hello(2,3)

#Q4
def Sum(args):
  tot=0
  for val in args:
    tot=tot+val
  print("Sum:",tot)    
l=[]
n=int(input("Number of elements:"))
for i in range(n):
  l.append(int(input("Enter values:"))) 
Sum(l)

#Q5
class Encapsulation:
  def __init__(self):
    self.originalValue=10

  def Value(self):
    return self.originalValue

  def setValue(self,newValue):
    self.originalValue=newValue
    return (self.originalValue)

obj=Encapsulation()
print("1st op ---->",obj.Value()) 
print("2nd op ---->",obj.setValue(100))

