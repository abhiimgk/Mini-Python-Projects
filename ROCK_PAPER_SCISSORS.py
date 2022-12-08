'''Rock Paper Scissors Game'''
import random
a=random.randint(1,3)
print("choose R,P,S for Rock,Paper and Scissors resepctively.")
i=0
ucount=0
ccount=0
while i<3:
    user=input("Enter your choice: ")
    if a==1:
        comp="R"
    elif a==2:
        comp="P"
    elif a==3:
        comp="S"
    if comp==user:
        print("computer chose",comp)
        print("user chose",user)
        print("It's a Draw")
    elif (user=="R" and comp=="S") or (user=="P"and comp=="R") or (user=="S" and comp =="P"):
        print("computer chose",comp)
        print("user chose",user)
        print("User wins!")
        ucount=ucount+1
    else:
        print("computer chose",comp)
        print("user chose",user)
        print("computer wins!")
        ccount=ccount+1
    i=i+1
if ucount>ccount:
    print("ucount:",ucount)
    print("ccount:",ccount)
    print("user wins the game")
elif ucount==ccount:
    print("ucount:",ucount)
    print("ccount:",ccount)
    print("It's a draw!")
else:
    print("ucount:",ucount)
    print("ccount:",ccount)
    print("computer wins the game")