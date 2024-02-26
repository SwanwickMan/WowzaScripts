from copy import copy
import keyboard
import os
clear = lambda: os.system('cls')

class cursor:
    def __init__(self,x,y,limit):
        self.x = x
        self.y = y
        self.limit = limit
        #create blank canvas and backup file
        lines = []
        for i in range(self.limit[1]+1):
            lines.append([" "]*(self.limit[0]+1))
        self.lines = lines
        self.backup = [lines[::-1],x,y]
    #input reference list
    dirList = {
        "w":[0,-1],
        "a":[-1,0],
        "s":[0,1],
        "d":[1,0]
        }
    funcList = {
        "esc":"self.save()",
        "space":"self.clear()",
        "enter":"self.saveState()",
        "backspace": "self.loadState()"
        }
    #move ball
    def move(self,key):
        #check for save or clear command
        if key not in ("w","a","s","d"):
            try:
                exec(self.funcList[key])
            except Exception as e:
                pass
        #move cursor
        self.x += self.dirList[key][0]
        self.y += self.dirList[key][1]
        #validate coordinates
        if self.x < 0:
            self.x = 0
        elif self.x > self.limit[0]:
            self.x = self.limit[0]
        if self.y < 0:
            self.y = 0
        elif self.y > self.limit[1]:
            self.y = self.limit[1]
    #update screen
    def update(self):
        clear()
        self.lines[self.y][self.x] = "o"
        for i in self.lines:
            print("".join(i))
        self.lines[self.y][self.x] = "x"
    #write to file
    def save(self):
        image = ""
        for i in self.lines:
            image += "".join(i)+"\n"
        with open("i am a gamer.txt","w") as g:
            g.write(image)
    #clear screen
    def clear(self):
        self.lines = []
        for i in range(self.limit[1]+1):
            self.lines.append([" "]*(self.limit[0]+1))
        self.update()
    #create save state
    def saveState(self):
        self.backup = [self.lines[::-1], self.x, self.y]
    #load save state and update screen
    def loadState(self):
        self.lines = self.backup[0][::-1]
        self.x, self.y = self.backup[1:]
        update(self)
        



x = cursor(1,1,[50,35])

while True:
    try:
        x.move(keyboard.read_key())
        x.update()
    except Exception as e:
        print(e)
