def solution(msg):
    answer = []
    lzw_dictionary = dict()
    
    for i in range(65, 91):
        lzw_dictionary[chr(i)] = i - 64
    
    index = 0
    while index < len(msg):
        next = msg[index]
        next_index = index + 1
        
        for i in range(index + 1, len(msg)):
            next += msg[i]
            if next not in lzw_dictionary:
                next_index = i
                break
        else:
            next_index = len(msg)
        current = msg[index : next_index]
        answer.append(lzw_dictionary[current])
        
        if next not in lzw_dictionary:
            lzw_dictionary[next] = len(lzw_dictionary) + 1
        
        index = next_index
        
    return answer