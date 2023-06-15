import pyautogui
from time import sleep
#sleep(3)
rows=int(input())
for i in range(rows):
    for j in range(i+1):
        pyautogui.write('# ')
    print("\n")
