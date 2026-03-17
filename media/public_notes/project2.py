import random

n = random.randint(1, 100)
a = -1

gusses = 0 

while (a != n):

    gusses +=1 

    a = int(input("Guess the numer : "))

    if(a>n):

        print("lower number please ")

    else:

        print("higher number please")

print(f"you have guessed the number {n} correctly in {gusses} attempts")