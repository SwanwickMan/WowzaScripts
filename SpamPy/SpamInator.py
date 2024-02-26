#TextFilinator


message = input("gamer input")
length = len(message)
loop = round(2000/(length+2))-1


try:
    g = open("text.txt", "x")
except:
    open("text.txt", "w").close()



f = open("text.txt", "a")

for i in range(loop):
    f.write(message + '\n')

f.close()


#open and read the file after the appending:
f = open("text.txt", "r")
print(f.read())
print("message =", message)
print("loops =", loop)


try:
    import clipboard
    r = open('text.txt', 'r')
    lines = r.readlines()
    limited_n_ints = ''
    for i in lines:
        limited_n_ints = limited_n_ints + i

    clipboard.copy(limited_n_ints)
    print("message attached to clipboard")
except:
    print("Failed To copy contents to clipboard, install clipboard module")

input(" ")
