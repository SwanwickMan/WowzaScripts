#PaperCup-Inator

#height of cups, 25cm
#cost of cups, £0.1398
#volume held by cups, 170.478ml
#area of cups is 19.6cm²
#Area used is 25cm² to simplify finding total area required for cup stack


#variables list
totalHeightcm = 0
number = 0
totalCups = 0
currentStack = 0
finalHeight = 0
totalVolume = 0
totalCost = 0
totalArea = 0

#Gather Height
finalHeight = int(input("How tall would you like the cup stack to be in centimeters"))


#run loop until cup stack height is larger than desird height
while totalHeightcm < finalHeight:
    
    #find and print results as found
    print(" ")
    number = number + 1
    print(number)
    currentStack = number ** 2
    print(currentStack)
    totalCups = currentStack + totalCups
    print(totalCups)
    
    print(" ")
    
    totalHeightcm = number * 25
    
#find and print results

print("        -=The results are in=-")
print(" ")

print(totalCups , ' would be the total cups used')

print(number , ' would be the number of cup stacks used')

totalCost = totalCups * 0.1398
totalCost = round(totalCost, 2)
print('£' , totalCost , 'would be the total cost of the cups')

totalVolume = totalCups * 170.478
totalVolume = round(totalVolume, 2)
print(totalVolume , 'ml would be the total volume of all the cups')

totalArea = currentStack * 25
print(totalArea , 'cm² would be the area required for the cup stack')

input(" ")
    
    
   




