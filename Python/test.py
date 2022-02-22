from random import *

customer = list(range(1,51))
count = 0
for i in customer:
    time = randint(5, 50)
    if 5<=time<=15:
        print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))
        count += 1
    else:
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))

print("총 탑승 승객 : {0} 명".format(count))
