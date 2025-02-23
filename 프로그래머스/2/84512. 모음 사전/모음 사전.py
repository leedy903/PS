dictionary = []
def solution(word):
    global dictionary
    answer = 0
    vowel = list("AEIOU")
    recur("", vowel)
    
    answer = dictionary.index(word) + 1
    
    return answer

def recur(string, vowel):
    global dictionary
    if len(string) == 5:
        return
    temp_string = string
    for i in range(5):
        temp_string = string + vowel[i]
        dictionary.append(temp_string)
        recur(temp_string, vowel)
        