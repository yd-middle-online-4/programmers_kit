import numpy as np

def solution(genres, plays):
    n = len(plays)
    
    total_play = {}
    play_list = {}
    
    for i in range(n):
        if genres[i] in total_play:
            total_play[genres[i]] += plays[i]
            play_list[genres[i]] += [[plays[i], n - i, i]]
        else:
            total_play[genres[i]] = plays[i]
            play_list[genres[i]] = [[plays[i], n - i, i]]
                       
    sorted_genres = sorted(total_play, key=lambda x:total_play[x], reverse=True)
            
    answer = []              
        
    for genre in sorted_genres:
        idx = np.array(sorted(play_list[genre], reverse=True))[:, 2]
        if len(idx) >= 2:
            answer += idx[:2].tolist()
        else:
            answer += idx.tolist()
            
    
   
    return answer