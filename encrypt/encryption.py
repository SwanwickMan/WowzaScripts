def genKey():
    import random as r
    f = open("primeList.txt", "r")
    primeList = f.read().splitlines()
    f.close()
    return(int(r.choice(primeList))*int(r.choice(primeList)))


#string stuff
def encryptString(message,key=False):
    if key == False:
        key = genKey()
    message = list(str(message))
    newMessage = []
    for i in message:
        newMessage.append(ord(i)*key)
    return(newMessage, key)

def decryptString(message,key):
    ogMessage = []
    try:
        for i in message:
            ogMessage.append(chr(int(int(i)/key)))
        s = ""
        for i in ogMessage:
            s += i
    except Exception as e:
        print(e)
    return(s)


#file stuff
def encryptFile(fileLocation,key=False):
    f = open(fileLocation, "rb")
    x = list(f.read())
    f.close()
    if key == False:
        key = genKey()
    g = open(fileLocation+".ale","w")
    g.write("")
    g.close()
    h = open(fileLocation+".ale","a")
    for i in x:
        h.write(str(int(i)*key)+",")
    return(key)

def decryptFile(fileLocation,key):
    f = open(fileLocation, "r")
    x = f.read().split(",")

    g = open("new"+fileLocation[:-4],"wb")
    for i in range(len(x)):
        try:
            x[i] = int(int(x[i])/int(key))
        except Exception as e:
            x.remove(x[i])
            print(e)
    g.write(bytearray(x))
    g.close()
