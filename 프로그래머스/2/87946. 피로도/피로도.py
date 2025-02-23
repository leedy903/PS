max_explore = 0
def solution(k, dungeons):
    answer = -1
    visit = [False for _ in range(len(dungeons))]
    
    recur(0, k, dungeons, visit)
    answer = max_explore
    
    return answer

def recur(index, gauge, dungeons, visit):
    global max_explore

    explore_count = visit.count(True)
    max_explore = max(max_explore, explore_count)
    if index == len(dungeons):
        return
    
    for i in range(len(dungeons)):
        if not visit[i] and dungeons[i][0] <= gauge:
            visit[i] = True
            recur(index + 1, gauge - dungeons[i][1], dungeons, visit)
            visit[i] = False

            
    