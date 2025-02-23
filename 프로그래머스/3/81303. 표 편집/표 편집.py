def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    
    neighbor_table = {i: [i - 1, i + 1] for i in range(n)}
    neighbor_table[0] = [None, 1]
    neighbor_table[n - 1] = [n - 2, None]
    
    delete_stack = []
    for command in cmd:
        if command == 'C':
            answer[k] = 'X'
            left, right = neighbor_table[k]
            delete_stack.append([left, k, right])
            
            if right == None:
                k = neighbor_table[k][0]
            else:
                k = neighbor_table[k][1]
                
            if right == None:
                neighbor_table[left][1] = None
            
            elif left == None:
                neighbor_table[right][0] = None
            
            else:
                neighbor_table[left][1] = right
                neighbor_table[right][0] = left
            
        elif command == 'Z':
            left, now, right = delete_stack.pop()
            answer[now] = 'O'
            
            if right == None:
                neighbor_table[left][1] = now

            elif left == None:
                neighbor_table[right][0] = now
                

            else:
                neighbor_table[left][1] = now                
                neighbor_table[right][0] = now
        
        else:
            command_type, distance = command.split(' ')
            distance = int(distance)
            if command_type == 'U':
                for _ in range(distance):
                    k = neighbor_table[k][0]
            elif command_type == 'D':
                for _ in range(distance):
                    k = neighbor_table[k][1]

    return "".join(answer)