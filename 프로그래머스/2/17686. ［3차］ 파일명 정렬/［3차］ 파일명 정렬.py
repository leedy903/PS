def solution(files):
    file_hash = dict()
    
    for file in files:
        str_index = 0
        while not file[str_index].isdigit():
            str_index += 1
            
        head = file[:str_index]
        
        int_index = str_index
        while int_index < len(file) and file[int_index].isdigit():
            int_index += 1
            
        number = file[str_index:int_index]
        
        file_hash[file] = [head.lower(), int(number)]
    
    file_hash = sorted(file_hash.items(), key = lambda x : (x[1][0], x[1][1]))
    answer = [file_name for file_name, _ in file_hash]   
    return answer