# A = 1 Z = 26

# def solution(name):
#     a = list(name)
#     b = []
#     cnt = 0
#     for i in range(len(a)):
#         a[i] = ord(a[i])-64
#         b.append(min(a[i],27-a[i]))
    
    
        
#     return a,b

# print(solution('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

# 모범답안

def solution(name):
    init_A = list("A"*len(name))
    name=list(name)
    TF=[]
    for a,b in zip(name,init_A):
        TF.append(a==b)  
    count=move_count(TF,0,0)
    for alpa in name:
        tmp=ord(alpa)-ord("A")
        count+=min(ord(alpa)-ord("A"),ord("Z")-ord(alpa)+1)
    return count


def move_count(TF,point,count):
    if sum(TF)==len(TF):
        return count
    else:
        tmp_all=[]
        target_index=[]
        tmp_TF=TF.copy()
        target_index_count=0
        
        while len(target_index) <= 1:
            if not TF[(point+target_index_count)%len(TF)]:
                target_index.append((point+target_index_count)%len(TF))
            if not TF[(point-target_index_count)%len(TF)]:
                target_index.append((point-target_index_count)%len(TF))
            target_index_count+=1
        #print("TF:",TF)
        #print("point:",point)
        #print("접근:",set(target_index))

        for i in set(target_index):
            if not TF[i]:
                tmp_TF=TF.copy()
                tmp_TF[i]=True
                tmp_all.append(move_count(tmp_TF,i,count+min(len(TF)-abs(point-i),abs(point-i))))
        return min(tmp_all)
    
print(solution("JEON"))