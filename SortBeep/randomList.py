try:
    import clipboard
    nonce = False
except:
    print("copy to clipboard failed")
    nonce = True
import random

num = int(input("length of array"))

list1 = []
for i in range(num):
    list1.append(random.randint(0,231))

if nonce == True:

    f = open("nonce.txt", "w")
    f.write(str(list1))
    f.close()

    input("contents saved to nonce.txt in same directory as this file")
else:
    clipboard.copy(str(list1))
    print(str(list1))
    input("copied to clipboard")
                 

