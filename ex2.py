a= int(input("please enter the first side of the triangle:" ))
b= int(input("please enter the second side of the triangle:" ))
c= int(input("please enter the third side of the triangle:" ))
if a+b>c and a+c>b and c+b>a:
    print("This is a triangle.")
else:
    print("It is not a triangle.")
   