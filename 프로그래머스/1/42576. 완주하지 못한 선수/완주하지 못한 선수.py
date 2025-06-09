def solution(participant, completion):
    answer = ''
    _hash = 0
    dic = {}
    
    for part in participant:
        dic[hash(part)] = part
        _hash += hash(part)
        
    for com in completion:
        _hash -= hash(com)
        
    answer = dic[_hash]
    return answer