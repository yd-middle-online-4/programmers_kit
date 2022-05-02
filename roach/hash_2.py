def solution(phone_book):
    answer = True
    phone_dict = {}
    
    for phone_num in phone_book:
        tmp = phone_dict
        for num in phone_num[:-1]:
            if num in tmp:
                tmp = tmp[num]
                if 'end' in tmp:
                    return False
            else:
                tmp[num] = {}
                tmp = tmp[num]
        
        if phone_num[-1] in tmp:
            tmp = tmp[phone_num[-1]]
            tmp['end'] = {}
            return False
        else:
            tmp[phone_num[-1]] = {}
            tmp = tmp[phone_num[-1]]
            tmp['end'] = {}
            
    
    return answer