import sys
input=sys.stdin.readline

n = int(input())

result = 0
for i in range(n):
    word = input()
    buf = {}
    result += 1
    for j in word:
        if j in buf.keys():
            if prev == j:
                continue
            result -= 1
            break
        buf[j] = True
        prev = j
print(result)