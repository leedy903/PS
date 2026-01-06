def solution(players, m, k):
    answer = 0
    server = 1
    timeline = [0 for _ in range(len(players) + k)]
    
    for i in range(len(players)):
        capacity = server * m - 1
        extra_server = 0
        if capacity < players[i]:
            extra_server = players[i] // m - server + 1
            timeline[i] += extra_server
            timeline[i + k - 1] -= extra_server
            answer += extra_server
        server += timeline[i]
    return answer