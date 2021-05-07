def solution(participants, completions):
    names = {}
        
    for participant in participants:
        if participant in names:
            names[participant] += 1
        else:
            names[participant] = 1
    
    for completion in completions:   
        names[completion] -= 1
        
             
    for player in participants:
        if names[player] > 0:
            return player



# 다른 사람 풀이

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]