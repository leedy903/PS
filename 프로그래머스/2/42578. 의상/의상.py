def solution(clothes):
    answer = 1
    clothes_hash = {}
    for item, kind in clothes:
        if kind in clothes_hash:
            clothes_hash[kind] += 1
        else:
            clothes_hash[kind] = 1
    
    for _, number in clothes_hash.items():
        answer *= (number + 1)
    
    return answer - 1