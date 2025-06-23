import random
n = random.randint(1,1000)

a = 0
guess = 1
while(a != n):
    a = int(input("Guess the corrent number: "))
    if(a > n):
        print("Lower number please")
        guess += 1
    elif(a < n):
        print("Higher number please")
        guess += 1

print(f"You have guessed the correct number {n} in {guess} attemps")


