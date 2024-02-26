#Brazilinator

def GetData():
    import subprocess
    Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
    a = str(Data)
    l = []
    try:
        for i in range(len(a)):
            l.append(a.split("\\r\\r\\n")[i])
            print(l[i])
    except IndexError as e:
        return(l)
    

def search(data):
    s = input("enter search term\n>>> ")
    for i in range(len(data)):
        if s in data[i]:
            print(data[i])

def kill():
    import os
    target = input("Which process would you like to kill\n>>> ")
    os.system('wmic process where name="'+target+'" delete')

#Validate input
def valInput(accept): # x = valInput(["yes","no"])
    while True:
        print("\nanswer one of the following:")
        for i in accept:
            print([i])
        x = input(">>> ")
        for i in accept:
            if x == i:
                print("    -----------=====================-----------")
                return(x)
        print("fuck off")

#Begin
data = GetData()
while True:
    ans = valInput(["kill","search","refresh","exit"])
    if ans == "kill":
        kill()
    elif ans == "search":
        search(data)
    elif ans == "refresh":
        data = GetData()
    else:
        break
