'''code for true FNV completionists only'''

#guess
class ExceptionHandlingButEpic(Exception):
        pass

#various ref dictionaries
uNum = {"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,
        "sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19
        }
sDigit = {"one":1,"two":2,"three":3,"four":4,"five":5,
        "six":6,"seven":7,"eight":8,"nine":9
        }
tens = {"ten":10,"twenty":20,"thirty":30,"forty":40,"fifty":50,
        "sixty":60,"seventy":70,"eighty":80,"ninety":90
        }           
hundreds = {"one hundred":100,"two hundred":200,"three hundred":300,"four hundred":400,"five hundred":500,
            "six hundred":600,"seven hundred":700,"eight hundred":800,"eight hundred":800,"nine hundred":900 
                }

#reversed dictionaries
uNumR = {v: k for k, v in uNum.items()}
sDigitR = {v: k for k, v in sDigit.items()}
sDigitR[0] = ""
tensR = {v: k for k, v in tens.items()}
tensR[0] = ""
hundredsR = {v: k for k, v in hundreds.items()}

'''bellow lists should be linked or bad stuff'''
sUnits = {"sextillion":10**21,"quintillon":10**18,"quadrillion":10**15,"trillion":10**12,"billion":10**9,"million":10**6,"thousand":1000}
sUnitsR = ("","thousand","million","billion","trillion","quadrillion","quintillon","sextillion")

#for string to number
def __toIntHundreds__(numPart):
        total = 0
        for n in (hundreds,uNum,tens,sDigit):
                for i in list(n.keys()):
                        if i in numPart:
                                numPart = numPart.replace(i,"")
                                total += n[i]
        return total

def strToInt(stringNumber):
        total = 0
        for i in sUnits:
                if i in stringNumber:
                        x = stringNumber.partition(i)
                        total += __toIntHundreds__(x[0])*sUnits[i]
                        stringNumber = stringNumber.replace(x[0]+x[1],"")
        total += __toIntHundreds__(stringNumber)
        if "negative" in stringNumber:return -total
        return total

#for number to string
def __toStrHundreds__(numPart):
        numPart = [int(i) for i in tuple(numPart)]
        if len(numPart) == 3 and numPart[0]==0:
            numPart.remove(0)
        name = []
        if len(numPart) == 3:
                if numPart[1] == 0 and numPart[2] == 0:
                        name.append(sDigitR[numPart[0]]+" hundred ")
                elif numPart[1] == 1 and numPart[2] > 0:
                        name.append(sDigitR[numPart[0]]+" hundred and "+uNumR[int(str(numPart[0])+str(numPart[1]))])
                else:
                        name.append(sDigitR[numPart[0]]+" hundred and "+tensR[numPart[1]*10]+" "+sDigitR[numPart[2]])
        elif len(numPart) == 2:
                if numPart[1] == 0 and numPart[1] > 0:
                        name.append(uNumR[int(str(numPart[0])+str(numPart[1]))])
                else:
                        name.append(tensR[numPart[0]*10]+" "+sDigitR[numPart[1]])
        else:
                return sDigitR[numPart[0]]
        return " ".join(name)      

def __intToLoL__(number):
        number = str(number)
        lst = []
        while number != "":
                x = number[-3:]
                lst.append(x)
                number = number[:-3]                
        lst.reverse()
        return lst

def intToStr(number):
        neg = ""
        if number > max(sUnits.values())*1000-1:
                raise ExceptionHandlingButEpic("your value is too epic and also too large for the code to COPE")
        elif number == 0:
                return "zero"
        elif number < 0:
                neg = "negative "
                number = abs(number)
        number = __intToLoL__(number)[::-1]
        name = []
        for i in range(len(number)):
                if __toStrHundreds__(number[i]) != " ":name.append(__toStrHundreds__(number[i])+" "+sUnitsR[i])
        return neg+" ".join(name[::-1])

#experimental floating point stuff (i hate floating point representation)
def floatToStr(number):
        integer = int(number)
        real = abs(number-integer)
        name = intToStr(integer)
        if real != 0:
                x = "point "
                print(str(real)[2:])
                for i in str(real)[2:]:
                        x += sDigitR[int(i)]+" "
        return name+x

#c af class
class number:
    def __init__(self,number):
        if type(number) == int:
                self.numName = intToStr(number)
                self.value = number
        elif type(number) == str:
                try:
                        self.numName = intToStr(int(number))
                        self.value = int(number)
                except:
                        print("gamer")
                        self.numName = number.lower()
                        self.value = strToInt(self.numName)
        else:
                raise ExceptionHandlingButEpic("your value is too epic and not an accepted type")
    def __repr__(self):
        return str(self.numName)
    def __str__(self):
        return("object storing string value of number "+numName)
    
    #math stuff (bad and repititive)
    def __add__(self,notSelf):
        return number(self.value+notSelf.value)
    def __sub__(self,notSelf):
        return number(self.value-notSelf.value)
    def __mul__(self,notSelf):
        return number(self.value*notSelf.value)
    def __floordiv__(self,notSelf):
        raise ExceptionHandlingButEpic("this only works with integer values you are floor dividing anyways you gremloid")
    def __truediv__(self,notSelf):
        return number(int(self.value/notSelf.value))
    def __mod__(self,notSelf):
         return number(self.value%notSelf.value)
    def __pow__(self,notSelf):
        return number(self.value**notSelf.value)
    #logic operators n shiet
    def __lt__(self,notSelf):
            if self.value < notSelf.value: return True
            return False
    def __le__(self,notSelf):
            if self.value <= notSelf.value: return True
            return False  
    def __eq__(self,notSelf):
            if self.value == notSelf.value: return True
            return False
    def __ne__(self,notSelf):
            if self.value != notSelf.value: return True
            return False
    def __ge__(self,notSelf):
            if self.value >= notSelf.value: return True
            return False

n=number


