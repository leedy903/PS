def solution(n, k):
    answer = 0
    MAX = int(1e7)
    prime_list = []
    prime_checklist = [True] * MAX
    for i in range(2, MAX):
        if prime_checklist[i]:
            for j in range(2, MAX//i):
                if prime_checklist[i * j]:
                    prime_checklist[i * j] = False
                    
    prime_checklist[0] = False
    prime_checklist[1] = False

    for i in range(2, MAX):
        if prime_checklist[i]:
            prime_list.append(i)
            
    del prime_checklist
    
    convert_num = []
    while n >= k:
        convert_num.append(n%k)
        n //= k
    convert_num.append(n)
    
    check_num = 0
    for index in range(-1, -len(convert_num) -1, -1):
        now = convert_num[index]
        print(now, end="")
        if now != 0:
            check_num *= 10
            check_num += now
            
        if now == 0 or index == -len(convert_num):
            if check_num < MAX and check_num in prime_list:
                answer += 1
            if check_num > MAX:
                for prime in prime_list:
                    if check_num % prime == 0:
                        check_num = 0
                        break
                else:
                    answer += 1
                    
            check_num = 0
    return answer