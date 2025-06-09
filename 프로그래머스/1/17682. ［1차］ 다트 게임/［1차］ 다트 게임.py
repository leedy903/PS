from collections import deque

def solution(dartResult):
    answer = 0
    scores = [0]
    results = parser(dartResult)
    print(results)
    bonus = {"S" : 1, "D" : 2, "T" : 3}
    option = {"*" : 2, "#" : -1}
    
    for result in results:
        score = ""
        for i, letter in enumerate(result):
            if result[i].isdigit():
                score += result[i]
                
            elif letter in bonus.keys():
                scores.append(pow(int(score), bonus[letter]))
                
            elif letter in option.keys():
                scores[-1] *= option[letter]
                if letter == "*":
                    scores[-2] *= 2
        print(scores)                
        
    
    answer = sum(scores)
    return answer

def parser(dartResult):
    results = []
    start = 0
    for i, letter in enumerate(dartResult):
        if letter in ("S", "D", "T"):
            if i + 1 < len(dartResult) and not dartResult[i + 1].isdigit():
                results.append(dartResult[start:i + 2])
                start = i + 2
            else:
                results.append(dartResult[start:i + 1])
                start = i + 1
    return results
            