def solution(arr):
    answer = []
    for num in arr:
        if answer and num == answer[-1]:
            continue
        answer.append(num)
    return answer