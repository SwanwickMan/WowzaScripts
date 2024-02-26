import os
clear = lambda: os.system('cls')
def loadBar():
    from time import sleep
    for i in range(10):
        with open(str(i+1)+".txt") as f:
            print(f.read())
        sleep(.5)
        clear()

loadBar()

while True:
    try:
        exec(input(">>>"))
    except Exception as e:
        print(e)
