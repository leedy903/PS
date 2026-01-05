def solution(storey):
    answer = 0
    while storey > 0:
        last = storey % 10
        if last > 5:
            answer += 10 - last
            storey += 10
        else:
            answer += last
        if last == 5 and storey % 100 >= 50:
            storey += 10
        storey //= 10
    return answer