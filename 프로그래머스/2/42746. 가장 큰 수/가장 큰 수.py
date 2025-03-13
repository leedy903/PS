def solution(numbers):
    if sum(numbers) == 0:
        answer = '0'
    else:
        answer = ''

        numbers = list(map(str, numbers))
        numbers.sort(key=lambda x: x*3, reverse=True)

        answer = answer.join(numbers)
    
    return answer