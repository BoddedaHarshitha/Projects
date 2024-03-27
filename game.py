import random
n=input("do you want play guessing game?Yes/No: ")
num=random.randint(0,100)
count=0
if n=="yes":
    while True:
        m=int(input("enter a number"))
        if m==num:
            print("your guess is correct u reach the target",)
            break
        elif m<num:
            print("your number is lesser than taget")
        else:
            print("your number is greater than taget")
            count=count+1
            if(count==5):
                print("Try Again Later")
                print("-------Game Over-------")
                break
else:
            print("-------Game Over-------")