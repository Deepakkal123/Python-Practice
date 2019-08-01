print("Enter a number")
z = int(input())
print("Enter a number 0 or 1")
booll = int(input())

if booll == 1:
    for z in range(0,z+1):
        print("*"*z)

elif booll == 0:
    for z in range(z,0,-1):
        print("*"*z)