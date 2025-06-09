from collections import Counter
def parser(string):
    pairs = []
    string = string.lower()
    
    for i in range(len(string) - 1):
        pair = string[i] + string[i + 1]
        if pair.isalpha():
            pairs.append(pair)
    
    return pairs
    

def solution(str1, str2):
    answer = 0
    
    str1_pairs = parser(str1)
    str2_pairs = parser(str2)
    
    str1_counter = Counter(str1_pairs)
    str2_counter = Counter(str2_pairs)
    
    str1_set = set(str1_pairs)
    str2_set = set(str2_pairs)
    
    intersection = str1_set & str2_set
    union = str1_set | str2_set

    intersection_value = 0
    for elem in intersection:
        intersection_value += min(str1_counter[elem], str2_counter[elem])
        
    union_value = 0
    for elem in union:
        union_value += max(str1_counter[elem], str2_counter[elem])
        
    answer = int((intersection_value / union_value) * 65536) if union_value != 0 else 65536
    
    return answer