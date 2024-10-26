from collections import Counter

def solution(participant, completion):
    answer = ''
    
    pc = Counter(participant)
    cc = Counter(completion)
    no = pc - cc
        
    return list(no.keys())[0]