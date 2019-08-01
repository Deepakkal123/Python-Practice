n=51
i=1
print("enter a number")
while(i<=10):

    inp = int(input())
    if inp == n:
        print("Winner winner chicken dinner: Number you entered is right with attempts remaning ", 10-i)
        break
    elif inp>51 and inp<60:
        print("You are very close")
    elif inp>51 and inp<55:
        print("You are now closest")
    elif inp>51 and inp<53:
        print("You are one step away")
    elif inp<51 and inp>49:
        print("You are one step away")
    elif inp<51 and inp>45:
        print("You are closest")
    elif inp<51 and inp>40:
        print("You are close")
    elif inp<=40:
        print("try a bigger number")
    elif inp>=60:
        print("try a smaller number")
    else:
        print("try again")
        break
    print("number of guesses remanining ", 10-i)
    i=i+1
    if i>10:
     print("game over : No chicken today")



