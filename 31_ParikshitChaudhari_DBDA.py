# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lHoS15kmVwScaZkb09TdMaTOYZpFTTyr
"""

#Q3
for i in range(1,6):
  for j in range(1,i+1):    
    print(j%2,end=" ")
  print()

#Q8
a='13567'
for i in range(0,len(a)):
  print(a[i]*(i+1))

#Q9
a=input("Enter String: ")
for i in a[1:len(a):2]:
  print(i,end='')

#Q10
while True:
  a=input(print("1)Accept 2 numbers\n2)Add\n3)Sub\n4)Mul\n5)Div\n6)Exit"))
  if a=='1':
    b=int(input("Enter 1st number: "))
    c=int(input("Enter 2nd number: "))
  elif a=='2':
    print("addition of",b,'and',c,'is',b+c)
  elif a=='3':
    print("Subtraction of",b,'and',c,'is',b-c)
  elif a=='4' :
    print("Multiplication of",b,'and',c,'is',b*c)
  elif a=='5':
    print("Division of",b,'and',c,'is',b/c)
  elif a=='6':
    print("Exit")
    break

#Q1
a = int(input("Enter hrs: "))
b = int(input("Enter mins: "))
print("seconds is",(a*60*60)+(b*60))

#Q5
class Maths:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def Add(self):
    print('Addition is :',(self.a)+(self.b))
  def Div(self):
    print('Division is :',(self.a)/(self.b))
  def Sub(self):
    print('Subtraction is :',(self.a)-(self.b))
  def Mul(self):
    print('Multiplication is :',(self.a)*(self.b))
m=Maths(10,15)

m.Add()

m.Div()

m.Sub()

m.Mul()

#2
a=int(input("Enter number: "))
b=['Zero','one','two','Three','Four','Five','Six','Seven','Eight','Nine']
for i in a:
  print(b[i])

#6
a=input("Enter a String: ")
d=l=s=0
for c in a:
  if c.isdigit():
    d=d+1
  elif c.isalpha():
    l=l+1
  else:
    s=s+1
    print("Letters",l)
    print('Digit',d)
    print('Symbol',s)

