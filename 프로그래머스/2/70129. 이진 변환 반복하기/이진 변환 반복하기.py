def solution(s):
    answer = [0, 0]
    while s != "1":
        one_count = s.count("1")
        answer[0] += 1
        answer[1] += len(s) - one_count
        s = bin(one_count)[2:]
        
    return answer