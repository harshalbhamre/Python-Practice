# name Harry, Rohan, Hammad
# For Harry - 1. Harry_Ex.txt , 2. Harry_di.txt
# same for others

def getdate():
  import datetime
  a = datetime.datetime.now()
  b = str(a)
  return b

while(1):

  while(1):  
    ch = input("Press 'A' to ADD data and 'R' to READ data : ")
    add = input("Press 'H' to ADD to HARRY, 'R' to add to ROHAN, 'HA' to ADD to HAMMAD : ")
    x = input ("press 'E' to enter EXERCISE and press 'D' to enter DIET : ")
    ent = input("Is this correct?(y/n) : "+ch+" , "+add+" , "+x+" : ")
    if (ent == 'y'):
      break
    elif(ent =='n'):
      continue

  if ch =='A' and add =='H' and x == 'E':
    print("Opening Harry_Ex.txt.....")
    f = open("Harry_Ex.txt", "a")
    data = input("Enter what you want to add : ")
    f.write("\n["+getdate()+"] "+data)
    f.close()
    print("\n["+getdate()+"] "+data+" : Added to the Harry_Ex.txt")

  elif ch =='A' and add =='H' and x == 'D':
    print("Opening Harry_Di.txt.....")
    f = open("Harry_Di.txt", "a")
    data = input("Enter what you want to add : ")
    f.write("\n["+getdate()+"] "+data)
    f.close()
    print("\n["+getdate()+"] "+data+" : Added to the Harry_Di.txt")

  elif ch =='A' and add =='R' and x == 'E':
    print("Opening Rohan_Ex.txt.....")
    f = open("Rohan_Ex.txt", "a")
    data = input("Enter what you want to add : ")
    f.write("\n["+getdate()+"] "+data)
    f.close()
    print("\n["+getdate()+"] "+data+" : Added to the Rohan_Ex.txt")

  elif ch =='A' and add =='R' and x == 'D': 
    print("Opening Rohan_Di.txt.....")
    f = open("Rohan_Di.txt", "a")
    data = input("Enter what you want to add : ")
    f.write("\n["+getdate()+"] "+data)
    f.close()
    print("\n["+getdate()+"] "+data+" : Added to the Rohan_Di.txt")

  elif ch =='A' and add =='HA' and x == 'E':
    print("Opening Hammad_Ex.txt.....")
    f = open("Hammad_Ex.txt", "a")
    data = input("Enter what you want to add : ")
    f.write("\n["+getdate()+"] "+data)
    f.close()
    print("\n["+getdate()+"] "+data+" : Added to the Hammad_Ex.txt")

  elif ch =='A' and add =='HA' and x == 'D':
    print("Opening Hammad_Di.txt.....")
    f = open("Hammad_Di.txt", "a")
    data = input("Enter what you want to add : ")
    f.write("\n["+getdate()+"] "+data)
    f.close()
    print("\n["+getdate()+"] "+data+" : Added to the Hammad_Di.txt")  

  elif ch =='R' and add=='H' and x=='E':
    print("***** Reading Harry_Ex.txt... *****")
    f = open("Harry_Ex.txt")
    print (f.read())
    f.close()
  
  elif ch =='R' and add=='H' and x=='D':
    print("***** Reading Harry_Di.txt... *****")
    f = open("Harry_Di.txt")
    print (f.read())
    f.close()

  elif ch =='R' and add=='R' and x=='E':
    print("***** Reading Rohan_Ex.txt... *****")
    f = open("Rohan_Ex.txt")
    print (f.read())
    f.close()

  elif ch =='R' and add=='R' and x=='D':
    print("***** Reading Rohan_Di.txt... *****")
    f = open("Rohan_Di.txt")
    print (f.read())
    f.close()

  elif ch =='R' and add=='HA' and x=='E':
    print("***** Reading Hammad_Ex.txt... *****")
    f = open("Hammad_Ex.txt")
    print (f.read())
    f.close()

  elif ch =='R' and add=='HA' and x=='D':
    print("***** Reading Hammad_Di.txt... *****")
    f = open("Hammad_Di.txt")
    print (f.read())
    f.close()

  else :
    print("Enter correct Input : ")
    
  yesNo = input("Do you want to start over?(y/n): ")
  if yesNo =='n':
    print("*** EXITING THE PROGRAM ***")
    break
  elif yesNo =='y':
    continue
