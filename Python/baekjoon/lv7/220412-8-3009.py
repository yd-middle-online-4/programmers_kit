# 일단 생각나는 대로 
import sys
input=sys.stdin.readline
axis = []

for i in range(3):
    axis.append(list(map(int,input().split())))

point1 = axis[0]
point2 = axis[1]
point3 = axis[2]
point4 = [0,0]


if point1[0] == point2[0]:
    point4[0] = point3[0]
elif point1[0] == point3[0]:
    point4[0] = point2[0]
elif point2[0] == point3[0]:
    point4[0] = point1[0]
    
if point1[1] == point2[1]:
    point4[1] = point3[1]
elif point1[1] == point3[1]:
    point4[1] = point2[1]
elif point2[1] == point3[1]:
    point4[1] = point1[1]
        
print(f"{point4[0]} {point4[1]}")
    