def solution(numbers, hand):
    answer = ''
    
    left_thumb = [3, 0]
    right_thumb = [3, 2]
    
    for number in numbers:
        thumb = ''
        y, x = divmod(number - 1, 3)
        if number in [1, 4, 7]:
            thumb = 'left'
        elif number in [3, 6, 9]:
            thumb = 'right'
        elif number in [2, 5, 8, 0]:
            if number == 0:
                y, x = 3, 1
            left = abs(left_thumb[0] - y) + abs(left_thumb[1] - x)
            right = abs(right_thumb[0] - y) + abs(right_thumb[1] - x)
        
            if left < right:
                thumb = 'left'
            elif left > right:
                thumb = 'right'
            else:
                thumb = hand
                
        if thumb == 'left':
            left_thumb = [y, x]
            answer += 'L'
        elif thumb == 'right':
            right_thumb = [y, x]
            answer += 'R'

    return answer