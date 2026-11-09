import os
import shutil
from pathlib import Path
# os.makedirs("values.txt" , exist_ok = True)
with open("values.txt" , "w") as f:
    f.write("10 3.5 7 hello")
with open('values.txt' , "r") as f:
    str = list(f.readline().split())
    for i in str:
        print(i)
with open('values.txt' , "a") as f:
    f.write(" 42")
with open('values.txt' , "r") as f:
    str = list(f.readline().split())
    sum = 0
    mn = 100
    mx = 0
    for i in str:
        if(i[0] != 'h'):
            x = int(float(i))
            sum += x
            mn = min(mn , x)
            mx = max(mx , x)
print(mn , mx , sum)