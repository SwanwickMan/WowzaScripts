#Input Validations
def valInput(accept): # x = valInput(["yes","no"])
    while True:
        print("answer one of the following:")
        for i in accept:
            print([i])
        x = input(">>> ")
        if x in accept:
            print(" ---=====---\n")
            return(x)
        print("invalid input\n")

def valRange(Min,Max):
    while True:
        try:
            answer = float(input("answer within the range: " + str(Min)+" to " + str(Max)+"\n>>> "))
            if answer >= Min and answer <= Max:
                return(answer)
            else:
                print("number outwith specified range")
        except:
            print("please input a number")

#Make thing iterator
class isIter:
    def __iter__(self):
        self.variables = list(vars(self).values())
        self.i = -1
        return self
    def __next__(self):
        try:
            self.i += 1
            return self.variables[self.i]
        except:
            raise StopIteration

#list array function   
def listAll(List): 
    for i in List:
        print(i)

#create dictionary
def declareTable(records):
    tempTable = {}
    for i in records:
        tempTable[i] = []
    return(tempTable)
      
#Navigate Files
def nav(path = False):
    import os, string
    if path != False:
        try:
            os.listdir(path)
            s = path
        except Exception as e:
            print(e)
            s = valInput(['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)])
    else:
        s = valInput(['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)])
        
    while True:
        #add //
        s += "\\"
        #Regular navigate
        if not "?" in s:
            print("current location: ",s)
            try:
                s += valInput(os.listdir(s)+["?full","?back","?return"])
            except Exception as e:
                print(e)
                s = valInput(['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)])
            #check if file
            if os.path.isfile(s):
                if valInput(["accept","back"]) == "accept":
                    return(s)
                else:
                    s = s.split("\\")[:-1]
                    s = "\\".join(s)
        #Type full location
        elif "full" in s.split("?")[1]:
            try:
                s = input("full location")
                os.listdir(s)
            except:
                print("not found")
        #Go back x places
        elif "back" in s.split("?")[1]:
            try:
                n = int(input("Go back how far?"))*-1
                s = s.split("\\")[:n-1]
                s = "\\".join(s)
            except:
                print("error")
                s = s.split("\\")[:-1]
                s = "\\".join(s)
                
        else:
            try:
                import clipboard as c
                c.copy(s)
            except:
                print("clipboard failed printing results\n",s)
            return(s)
    bytearray
