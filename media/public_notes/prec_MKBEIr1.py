import random
import time

#  1 :

# print("1 for addition ")
# print("2 for substraction")
# print("3 for multiplication")
# print("4 for divide")

# select =  input("enter the number : ")

# num1 = float(input("enter the number : "))
# num2 = float(input("enter the number : "))

# if select == "1" :
#     print(num1+num2)

# elif select == "2" :
#     print(num1-num2)

# elif select == "3" :
#     print(num1*num2)

# elif select == "4" :
#     if num2 != 0 :
#         print(num1/num2)
#     else :
#         print("error")
    
# else : 
#     print("invalid")

# 2 :

# n = int(input("enter the number : "))

# for i in range(1,11) :
#     print(f"{n} X {i} = {n*i}")

# 3 :

# num = int(input("enter the number : "))

# if num %2 == 0 :
#     print("the given number is even ")

# else :
#     print("the given number is odd ")





# choice = random.randint(1,10)

# ychoice =int(input("enter your number : "))

# if ychoice==choice :
#     print("you are right")
#     print(f"the system number is {choice} same as you guessed")

# else :
#     print("you are wrong , tyr again")





# print("welcome to russian roulette")

# chambers = 6

# bullet_position = random.randint(1,chambers)

# current_chamber = 1

# while True :
#     input("press enter to pull the trigger : ")

#     if current_chamber == bullet_position :
#         print("you are died")
#         break


#     else:

#         print("you are lucky")

#     current_chamber += 1

# print(f"the bullet is on {bullet_position} place ")
    



choice = random.randint(1,10)

while True :
    y=int(input("enter the number : "))
    
    if y==choice :
        print("you are right")
        break

    elif y==choice-1 or y==choice-3 :
        print("you are too close , try again")

    else :
        print("you are wrong , try agin")






