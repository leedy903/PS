def show_matrix(matrix):
    MAX = str(max(map(max, matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            now = str(matrix[i][j])
            space = len(MAX) - len(now)
            print(" "*space + now, end=" ")
        print()
    print()   

def solution(alp, cop, problems):
    INF = 100000
    max_alp = 0
    max_cop = 0
    max_cost = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
        
    cost_map = [[INF for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
        
    problems.append([0, 0, 0, 1, 1])
    problems.append([0, 0, 1, 0, 1])
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    cost_map[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            for problem in problems:              
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp)
                    new_cop = min(j + cop_rwd, max_cop)
                    cost_map[new_alp][new_cop] = min(cost_map[new_alp][new_cop], cost_map[i][j] + cost)
                    
    answer = cost_map[max_alp][max_cop]
    return answer