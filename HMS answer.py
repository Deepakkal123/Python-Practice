import datetime
def getdt():
    return datetime.datetime.now()

def take():
    print("1 for Deep, 2 for roh, 3 for Adi")
    g=int(input())
    if g == 1:
        print("HMS for deep")
        print("Enter 1 for E and 2 for F")

        m =int(input())
        if m == 1:
            value = input("type value\n")
            with open ("Deepak-E ","a") as f:
                f.write(str([str(getdt())]) + ": " + value + "\n")
                print("success")
        else:
            value = input("type value\n")
            with open("Deepak-Food ", "a") as f:
                f.write(str(str(getdt()), value))
                print("success")
    elif g == 2:
        print("HMS for Rohan")
        print("Enter 1 for E and 2 for F")

        m = int(input())
        if m == 1:
            value = input("type value\n")
            with open("rohan-E ", "a") as f:
                f.write(str(str(getdt()), value))
                print("success")
        else:
            value = input("type value\n")
            with open("rohan-Food ", "a") as f:
                f.write(str(str(getdt()), value))
                print("success")
    elif g == 3:
        print("HMS for Addu")
        print("Enter 1 for E and 2 for F")

        m = int(input())
        if m == 1:
            value = input("type value\n")
            with open("Addu-E ", "a") as f:
                f.write(str(str(getdt()), value))
                print("success")
        else:
            value = input("type value\n")
            with open("Addu-Food ", "a") as f:
                f.write(str(str(getdt()), value))
                print("success")
    else:
        print("Invalid output")

def Retrive():
    print("1 for Deep, 2 for roh, 3 for Adi")
    g = int(input())
    if g == 1:
        print("HMS for deep")
        print("Enter 1 for E and 2 for F")

        m = int(input())
        if m == 1:
            with open("Deepak-E ") as f:
                for i in f:
                    print(i)

        else:

            with open("Deepak-Food ") as f:
                for i in f:
                    print(i)

    elif g == 2:
        print("HMS for Rohan")
        print("Enter 1 for E and 2 for F")

        m = int(input())
        if m == 1:
            with open("Rohan-E ") as f:
                for i in f:
                    print(i)

        else:

            with open("Rohan-Food ") as f:
                for i in f:
                    print(i)
    elif g == 3:
        print("HMS for Addu")
        print("Enter 1 for E and 2 for F")

        m = int(input())
        if m == 1:
            with open("addu-E ") as f:
                for i in f:
                    print(i)

        else:

            with open("addu-Food ") as f:
                for i in f:
                    print(i)
    else:
        print("Invalid output")



print("HMS")
print("Enter 1 for log and 2 for view")
a=int(input())
if a == 1:
    print("Enter value")
    take()

else:
    Retrive()