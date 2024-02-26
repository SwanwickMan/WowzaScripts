import winsound as w
import random,time,os
#w.PlaySound("*", w.SND_ALIAS)

f = open("perm.txt","r")
tempList = f.readlines()
f.close()

list1 = ("memory","permission", "file","hash")
while True:
    choice = random.choice(list1)
    print("\n")
    if choice == "memory":
        for i in range(17):
            print("value at memory address : "+str(hex(random.randint(1,100000000)))[:8])
    elif choice == "permission":
        for i in range(7):
            print("permission error: "+random.choice(tempList)[:-1])
    elif choice == "file":
        try:
            for i in os.listdir("N:\\"):
                print(i)
        except Exception as e:
            print(e)
    else:
        for x in range(13):
            hash1 = ""
            for i in range(14):
                hash1 += chr(random.randint(0,128))
            print(" hash for user "+ hash1 + str(x+1))

    w.PlaySound("*", w.SND_ALIAS)
