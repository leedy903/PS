def solution(N, number):
    answer = -1
    dp = []
    for n_length in range(1, 9):
        n_case = set()
        n_num = int(str(N) * n_length)
        n_case.add(n_num)
        
        for i in range(n_length - 1):
            for op1 in dp[i]:
                for op2 in dp[-1 - i]:
                    n_case.add(op1 + op2)
                    n_case.add(op1 * op2)
                    if op1 >= op2:
                        if op1 != op2:
                            n_case.add(op1 - op2)
                        if op2 != 0:
                            n_case.add(op1 // op2)
                        
        if number in n_case:
            answer = n_length
            break
        
        dp.append(n_case)
        
    return answer