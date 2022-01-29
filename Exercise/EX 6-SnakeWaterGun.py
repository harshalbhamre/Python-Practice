import random

print("Welcome to Snake Water Gun Game :  ")
list1 = ["Snake", "Water", "Gun"]
i = 10
uscore = 0
pscore = 0
while i>0:
    print("number of tries remaining : ", i)
    i -=1
    pc = random.choice(list1)
    user = input("Enter your choice S for Snake, W for Water and G for Gun  :  ")
    if user== 'S' and pc== 'Snake':
        print("pc chose Snake...")
        print("no Score(tie)")
    elif user== 'S' and pc== 'Water':
        print("pc chose Water!")
        print("YOU WON!!!")
        uscore +=1
    elif user== 'S' and pc== 'Gun':
        print("PC chose GUN!")
        print("YOU LOST!")
        pscore +=1
    elif user== 'W' and pc== 'Snake':
        print("PC CHOSE SNAKE")
        print("YOU LOST!")
        pscore +=1
    elif user== 'W' and pc== 'Water':
        print("PC CHOSE WATER")
        print("TIE!!")
    elif user== 'W' and pc== 'Gun':
        print("PC CHOSE GUN")
        print("GUN WAS LOST IN THE WATER")
        print("YOU WON!!!")
        uscore +=1
    elif user== 'G' and pc== 'Snake':
        print("PC CHOSE SNAKE")
        print("SNAKE WAS KILLED BY GUN FIRE")
        print("YOU WON!!!")
        uscore +=1
    elif user == 'G' and pc == 'Water':
        print("PC CHOSE WATER")
        print("GUN WAS LOST IN THE WATER")
        print("YOU LOST!")
        pscore +=1
    elif user == 'G' and pc == 'Gun':
        print("PC CHOSE GUN")
        print("TIE!!")
    else :
        print("invalid input :")
    print("Total Score : ", end=" ")
    print("YOUR SCORE = ", uscore, end=" ")
    print("PC's SCORE = ", pscore)

if uscore>pscore:
    print("YOU WON THE MATCH !!!!")

elif pscore>uscore:
    print("YOU LOST THE MATCH!")

elif pscore==uscore:
    print("ITS A TIE!!")
else:
    print("ERROR OCCURED")
