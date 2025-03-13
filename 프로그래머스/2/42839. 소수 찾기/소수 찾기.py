from itertools import permutations as permu

def solution(numbers):
    
    MAX = 10000000
    
    answer = set()
    
    num_papers = []
    
    prime_nums = [True] * MAX
    
    prime_nums[0] = False
    prime_nums[1] = False
    
    for i in range(2, MAX):
        if prime_nums[i]:
            for j in range(i, MAX//i):
                if prime_nums[i * j]:
                    prime_nums[i * j] = False
                    
    for num in numbers:
        num_papers.append(int(num))
    
    for i in range(1, len(num_papers) + 1):
        permu_cases = list(permu(num_papers, i))
        
        for num_case in permu_cases:            
            check_num = 0
            for j, num in enumerate(num_case):
                check_num += num * pow(10, j)
            if prime_nums[check_num]:
                answer.add(check_num)

    return len(answer)