import random
list=("Snake","water","gun")
picked=random.choice(list)
print(picked)

print("Welcome to the game of snake water gun")
print("You will get a total of 10 attempts to beat your enemy")
i=1
while(i<=10):



    print("enter your choice:attempt-",i)
    G=input()
    if picked==G:

        print(f"You beat your enemy{G}")
        #for count in range(0,10):
        #count = count + 1
         #print(count)


    else:
        print(f"you lost{G}")
        C=0
        C=C+1
        print(C)
    i=i+1






