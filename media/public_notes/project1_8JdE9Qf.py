import random

computer = random.choice([-1,0,1])

you = input("enter your number : ")
dic = {"s" : -1 , "w" : 1 , "g" : 0}
rdic = {-1 :"stone",1:"paper",0:"scissor"}

youstr = dic[you]
print(f"you chose {rdic[youstr]}\ncomputer chose {rdic[computer]}")

if computer == youstr :
    print("Drow")

else :
    if computer==0 and youstr==1 :
        print("you lose")

    elif computer==0 and youstr==-1 :
        print("you win")
    
    elif computer==1 and youstr==0 :
        print("you win")

    elif computer==1 and youstr==-1 :
        print("you lose")

    elif computer==-1 and youstr==0 :
        print("you lose")

    elif computer==-1 and youstr==1 :
        print("you win")

    else :
        print("something went wrong ")
      

# import random

# dic = {"s": -1, "w": 1, "g": 0}
# rdic = {-1: "stone", 1: "paper", 0: "scissor"}

# while True:
#     computer = random.choice([-1, 0, 1])
#     you = input("Enter your choice (s = stone, w = paper, g = scissor): ")

#     if you not in dic:
#         print("Invalid input, try again.\n")
#         continue

#     youstr = dic[you]

#     print(f"You chose {rdic[youstr]}")
#     print(f"Computer chose {rdic[computer]}")

#     if computer == youstr:
#         print("Draw! Try again.\n")

#     else:
#         if computer == 0 and youstr == 1:
#             print("You lose!\n")

#         elif computer == 0 and youstr == -1:
#             print(" You win!")
#             break

#         elif computer == 1 and youstr == 0:
#             print(" You win!")
#             break

#         elif computer == 1 and youstr == -1:
#             print("You lose!\n")

#         elif computer == -1 and youstr == 0:
#             print("You lose!\n")

#         elif computer == -1 and youstr == 1:
#             print(" You win!")
#             break
