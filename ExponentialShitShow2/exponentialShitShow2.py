import random

score = 0
difficulty = 0
answer = float(random.randint(3,9))
randNum = 1


while True:
    try:
        while difficulty <= 1:
            difficulty = float(input("input difficulty as a positive integer larger than 1, 9 is reccomended"))
        break        
    except:
        print("type a positive integer larger than 1 you spaztard")

while True:
    randNum = float(random.randint(1, difficulty))
    function = {"mult": randNum * answer,"add":randNum + answer}
    functionStr = {"mult": str(randNum) + " * " + str(answer),
                   "add":str(randNum) + " + " + str(answer)}
    
    answer = random.choice(list(function.values()))
    print(functionStr[list(function.keys())[list(function.values()).index(answer)]])
    print(" ")

    try:
        playerAnswer = float(input("your answer    "))
    except:
        break

    if answer == playerAnswer:
        score = score + 1
        print("welldone your score multiplier is now ", score)
    else:
        print(" ")
        print("you lose")
        print("the answer was", answer)
        break
        
finalscore  = round(score * (answer/100), 2)
print("your final score is ", finalscore)

#scoreboard
f = open("scores", "r")
scoreList = f.read().split(",")
f.close

for x in range(len(scoreList)):
    if finalscore > float(scoreList[x]):
        scoreList.append(str(finalscore))
        scoreList.sort(reverse = True, key=float)
        del scoreList[3:]
        break
g = open("scores", "w")
g.write(",".join(str(x) for x in scoreList))
g.close()

print(" ")
print("top scores for all time")
for x in scoreList:
    if float(x) == finalscore:
        print(x, "<--your score")
    else:
        print(x)
input(" ")


