import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    banned_cases = set()
    
    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace("*", ".")
        
    ban_size = len(banned_id)
    for test_case in permutations(user_id, ban_size):
        ban_count = 0
        for u_id, b_id in zip(test_case, banned_id):
            p = re.compile(b_id)
            if p.match(u_id) and len(u_id) == len(b_id):
                ban_count += 1
        if ban_count == ban_size:
            banned_cases.add(tuple(sorted(test_case)))
    answer = len(banned_cases)
    return answer