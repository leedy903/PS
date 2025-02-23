import re
def solution(new_id):
    special_character = '~!@#$%^&*()=+[{]}:?,<>/'
    
    # step 1
    new_id = new_id.lower()
    answer = new_id[:]
    
    # step 2
    for c in new_id:
        if c in special_character:
            answer = answer.replace(c, '')
    
    # step 3
    answer = re.sub('[.]+', '.', answer)
    
    # step 4
    answer = answer.strip('.')
    
    # step 5
    if len(answer) == 0:
        answer = 'a'
    
    # step 6
    answer = answer[:15]
    answer = answer.rstrip('.')
    
    # step 7
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
                
    return answer