import os, sys
from random import randint

def rand():
    dd=[]
    while True:
        dd.append(str(randint(1, 45)).zfill(2))
        dd = list(set(dd))
        if len(dd)==6:
            break       
    print(sorted(dd))    

f = open('복권저장.txt','w')
sys.stdout = f

for i in range(5):
    rand()

sys.stdout = sys.__stdout__
f.close()

print("복권 생성 완료")
os.system("pause")