import os
import time
 
while True:
    os.system('wmic process where name="Notepad.exe" delete')
    time.sleep(1)
