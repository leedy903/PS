from itertools import permutations as permu
def solution(expression):
    max_number = 0
    operator = ['*', '+', '-']
    operator_cases = list(permu(operator, 3))
    for operator_case in operator_cases:
        operator_case = list(operator_case)
        max_number = max(max_number, abs(parser(expression, operator_case, 0)))
    answer = max_number
    return answer

def parser(expression, operators, index):
    numbers = []
    if index == 3:
        return int(expression)
    
    operator = operators[index]
    for parsed in expression.split(operator):
        if parsed.isdigit():
            numbers.append(int(parsed))
        else:
            numbers.append(parser(parsed, operators, index + 1))
    
    if operator == '+':
        result = sum(numbers)
    elif operator == '-':
        if numbers != []:
            result = numbers[0]
            for number in numbers[1:]:
                result -= number
        else:
            result = 0

    elif operator == '*':
        result = 1
        for number in numbers:
            result *= number
            
    return result
    
        