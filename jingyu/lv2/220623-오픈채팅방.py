from collections import defaultdict as d
def solution(record):
    dict = d(list)
    process = []
    result = []
    for words in record:
        word = list(words.split(' '))
        process.append((word[0],word[1]))
        if len(word) > 2:
            dict[word[1]].append(word[2])
        
    for i in range(len(process)):
        if process[i][0] == 'Enter':
            result.append("%s님이 들어왔습니다." %dict[process[i][1]][-1])
        elif process[i][0] == 'Leave':
            result.append("%s님이 나갔습니다." %dict[process[i][1]][-1])

    
    return result

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])