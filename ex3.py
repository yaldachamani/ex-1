a= input("please enter your first name: ")
b= input("please enter your family: ")
c= int(input("please enter your grade of the first lesson: "))
d= int(input("please enter your grade of the second lesson: "))
e= int(input("please enter your grade of the third lesson: "))
f=(c+d+e)/3
if f>=17:
    print("your name is",a,"\nyour family is ",b,"\nyour average is Greate")
if f<17 and f>=12:
    print("your name is",a,"\nyour family is ",b,"\nyour average is Normal")    
if f<12:
    print("your name is",a,"\nyour family is ",b,"\nyou Failed")    