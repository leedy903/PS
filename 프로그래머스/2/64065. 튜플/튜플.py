def solution(s):
    answer = []
    s = s[1:-1]
    s = s.split(',')
    number_hash = dict()
    
    for string in s:
        if string[0] == '{':
            string = string[1:]
            
        if string[-1] == '}':
            string = string[:-1]
            
        number = int(string)
         
        if number not in number_hash:
            number_hash[number] = 1
        else:
            number_hash[number] += 1
                
    number_rank = sorted(number_hash.items(), key = lambda x : x[1], reverse = True)
    answer = [number for (number, rank) in number_rank]
    
    return answer