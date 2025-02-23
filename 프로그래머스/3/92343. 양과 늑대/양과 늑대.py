max_sheep = 0
def solution(info, edges):
    answer = 0
    tree = [] # [sheep or wolf, left, right]
    visit = [False] * len(info)
    for i, animal in enumerate(info):
        has_left = False
        left = None
        right = None
        for j in range(len(edges)):
            if edges[j][0] == i:
                if has_left:
                    right = edges[j][1]
                    edges[j][0] = -1
                    break
                    
                left = edges[j][1]
                edges[j][0] = -1
                has_left = True
        tree.append([left, right])

        
    def collect(index: int, sheep: int, wolf: int, visit: list) -> int:
        global max_sheep
        visit[index] = True
        
        # 양, 늑대 개수 갱신
        animal = info[index]
        if animal == 0:
            sheep += 1
        elif animal == 1:
            wolf += 1
        
        max_sheep = max(max_sheep, sheep)
        
        # 방문한 node의 자식 node들을 방문할 수 있는지 확인
        nexts = []
        for node, is_visited in enumerate(visit):
            if is_visited:
                left, right = tree[node]
                if left and not visit[left] and sheep > wolf + info[left]:
                    nexts.append(left)

                if right and not visit[right] and sheep > wolf + info[right]:
                    nexts.append(right)
                            
        # 더 이상 갈 수 있는 node가 없으면 stop
        if nexts == []:
            return
        
        # 더 갈 수 있다면 재귀
        for _next in nexts:
            collect(_next, sheep, wolf, visit)
            visit[_next] = False
        
    collect(0, 0, 0, visit)
    answer = max_sheep
    return answer