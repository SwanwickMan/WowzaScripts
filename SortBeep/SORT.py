import winsound
list1 = [3, 10, 7, 108, 138]

for x in list1:
    print("|"*x)

print(" ")

for x in range(len(list1)):
    print(x)
    for i in range(len(list1)):
        if list1[x] < list1[i]:
            temp = list1[x]
            list1[x] = list1[i]
            list1[i] = temp
            winsound.Beep(list1[x]+274, 500) #number after comma = beep length in milliseconds
        for n in list1:
            print("|"*n)
        print(" ")

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
input(" ")
