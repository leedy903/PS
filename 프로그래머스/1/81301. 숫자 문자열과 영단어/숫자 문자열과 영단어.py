def solution(s):
    answer = ''
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet_number = {'zero' : '0',
                       'one' : '1',
                       'two' : '2',
                       'three' : '3',
                       'four' : '4',
                       'five' : '5',
                       'six' : '6',
                       'seven' : '7',
                       'eight' : '8',
                       'nine' : '9'}
    alphabet = ''
    for char in s:
        if char in number:
            answer += char
        else:
            alphabet += char
            if alphabet in alphabet_number:
                answer += alphabet_number[alphabet]
                alphabet = ''
    return int(answer)