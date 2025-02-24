def solution(triangle):
    answer = 0
    
    for i, row in enumerate(triangle):
        if i == 0:
            continue
        pre_row = triangle[i - 1]
        for j, num in enumerate(row):
            if j == 0:
                row[j] += pre_row[j]
            elif j == len(row) - 1:
                row[j] += pre_row[j - 1]
            else:
                row[j] += max(pre_row[j -1], pre_row[j])
    
    answer = max(triangle[-1])    
    
    return answer