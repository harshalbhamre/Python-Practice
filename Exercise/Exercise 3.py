#n = 18

t = 9

while (1) :

  while (t > 0) :

  

    print ("guesses Left : ", t)

    g = int(input("Guess the Number : "))

  

    if (g > 18) :

      print ("your Guess is HIGHER than the number :")

      t = t - 1

      continue

    

    elif (g < 18) :

      print ("Your Guess is LOWER than than the number")

      t = t - 1

      continue

 

    elif (g == 18) :

      print ("Congratulations Your guess is Correct!")

   

  print ("Sorry you ran out of Guesses")

  ch = input("do you want to try again (y/n)?")

  if (ch == "y") :

    t = 9 

    continue

  elif (ch == "n") :

    print ("Exiting ...")

    break

  else :

    print ("please check you input")

    
