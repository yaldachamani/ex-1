
op= input("please enter operation: ")
import math
sin= math.sin
cos= math.cos
tan= math.tan
factorial= math.factorial
if op=="+":
    a= int(input("please enter first number: "))
    b= int(input("please enter second number: "))
    result=a+b
if op=="-":
    a= int(input("please enter first number: "))
    b= int(input("please enter second number: "))
    result=a-b
if op=="*":
    a= int(input("please enter first number: "))
    b= int(input("please enter second number: "))
    result=a*b
if op=="/":
    a= int(input("please enter first number: "))
    b= int(input("please enter second number: "))
    if b==0:
      result= "please enter another b"
    if b!=0:
     result=a/b
if op=="radical":
    a= int(input("please enter the number: "))
    result= a**(1/2)
if op=="factorial":
    a= int(input("please enter the number: "))
    result=factorial(a)
if op=="sin":
    a= int(input("please enter the number: "))
    result=sin(math.radians(a))
if op=="cos":
    a= int(input("please enter the number: "))
    result=cos(math.radians(a))
if op=="tan":
    a= int(input("please enter the numbe: "))
    result=tan(math.radians(a))
if op=="cot":
    a= int(input("please enter the number: "))
    result=(math.cos(math.radians(a)))/(math.sin(math.radians(a)))
 
print(result)               