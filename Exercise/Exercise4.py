"""
print patttern
input = an integer n
boolean = true or false
 if true then print and n=5

*
**
***
****

else print

****
***
**
*

"""

n = int(input("Enter your number of rows : "))
x = input("are you a robot(y/n)? ")
if x == "y":
    t = True
    print(t)
elif x=="n":
    t = False
    print(t)
else:
    print("Enter y/n...")

if t== True:
    for i in range(1,n):
        for j in range(1,i+1):
            print("*",end="")
        print("\r")

elif t== False:
    for i in range(n,1,-1):
        for j in range(1,i+1):
            print("*",end="")
        print("\r")


