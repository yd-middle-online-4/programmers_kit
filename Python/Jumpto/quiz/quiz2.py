from logging import exception
from os import sep
from random import *

lst = ["apple", "banana", "orange"]
ran_num = randint(0, 2)
discovered = []
status = True

for i in lst[ran_num]:
    discovered.append("_")
print(' '.join(discovered))
un_dis_num = discovered.count('_')

while status == True:
    try:
        answer = input('1글자를 입력하세요 : ')
        counter = lst[ran_num].count(answer)
        location = lst[ran_num].index(answer)
        if counter > 0 and un_dis_num > 0:
            print("Correct")
            discovered[location] = answer
            print(' '.join(discovered))
            counter = 0
        elif counter <= 0:
            print("Wrong")
        else:
            print("SUCCESS")
            status = False
            
    except Exception as e:
        print("잘못된 값입니다. 다시 입력하세요")