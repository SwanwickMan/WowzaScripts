import subprocess
 
Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(Data)
try:
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[i])
except IndexError as e:
    input("gamer")
