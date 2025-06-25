#                                      GAME: STONE,PAPPER,SCISSOR.
# we taking:
# stone as : 0
# papper as : 1
# scissor as : -1

import random
print("let's play the game.")
computer=random.choice([0,1,-1])
user=input("enter your choice: ")
a={"stone":0,"papper":1,"scissor":-1}
b={0:"stone", 1:"papper", -1:"scissor" }
usernum=a[user]
print(f"comp chose {b[computer]}.\n you chose {b[usernum]}.")
if(computer==usernum):
    print("draw")
elif(computer==0 and usernum==-1):
    print("you lose")
elif(computer==0 and usernum==1):
    print("you win")
elif(computer==1 and usernum==-1):
    print("you win")
elif(computer==1 and usernum==0):
    print("you lose")
elif(computer==-1 and usernum==0):
    print("you win")
elif(computer==-1 and usernum==1):
    print("you lose")   
else:
    print("error")       