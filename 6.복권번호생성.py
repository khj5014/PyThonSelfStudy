import os
from random import *


# # 복권 방법 1
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# # 복권 방법 2
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# # 복권 방법 3

# for i in 범위(5nt(randint(1, 45)) # 1~ 46 미만의 임의의 값 생성
def rand():
    dd=[]
    while True:
        dd.append(str(randint(1, 45)).zfill(2))
        dd = list(set(dd))
        if len(dd)==6:
            break       
    print(sorted(dd))

for i in range(5):
    rand()
    
os.system("pause")