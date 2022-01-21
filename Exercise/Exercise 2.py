#python 3.7.1

z = 0

print ("Enter Two noumbers : ")

x = float(input("Enter your first number: "))

y = float(input("Enter your Second Number : "))

ch = input("select what you want to do? (+,-,*,/) : ")

if (x==45 or x==3 and y==3 or y==45 and ch=='*') :

  print ("your Multiplication is : 555")

  

elif (x==56 and y==9 and ch=='+') :

  print("Your Addition is : 77")

  

elif (x==56 and y==6 and ch=='/') :

  print("Your Division is : 4")

  

elif (ch=='+') :

  z = x + y

  print("your Addition is : ", z)

  

elif (ch== '-') :

  z = x - y 

  print("Your Substraction is : ", z)

  

elif (ch == '*') :

  z = x * y

  print("your Multiplication is : ", z)

  

elif (ch == '/') :

  z = x / y

  print("Your Division is : ", z)

  

else :

  print("invalid input")

