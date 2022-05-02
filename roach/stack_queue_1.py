import numpy as np
def solution(progresses, speeds):
    progresses = np.array(progresses)
    speeds = np.array(speeds)
    answer = []
    
    while len(progresses) > 0:
        
        count =0
        progresses += speeds
        while len(progresses) > 0:
            if progresses[0] >= 100:
                count += 1
                progresses = progresses[1:]
                speeds = speeds[1:]
            else:
                break
        
        if count != 0:
            answer.append(count)
            
    return answer