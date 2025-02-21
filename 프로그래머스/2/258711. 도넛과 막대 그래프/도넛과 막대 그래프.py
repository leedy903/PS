from collections import Counter
def solution(edges):
    answer = [0, 0, 0, 0]
    outcome_degree = Counter([a for a, b in edges])
    income_degree = Counter([b for a, b in edges])
    
    nodes = set(list(outcome_degree.keys()) + list(income_degree.keys()))

    for node in nodes:
        if outcome_degree[node] >= 2 and income_degree[node] == 0:
            answer[0] = node
        elif outcome_degree[node] == 2 and income_degree[node] >= 2:
            answer[3] += 1
        elif outcome_degree[node] == 0:
            answer[2] += 1
    
    answer[1] = outcome_degree[answer[0]] - answer[2] - answer[3]
    
    return answer