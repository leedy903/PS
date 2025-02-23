def solution(places):
    
    def find_p(depth: int, place: list, visit: list, y: int, x: int) -> bool:
        result = []
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        visit[y][x] = True
        
        if depth != 0 and place[y][x] == 'P':
            return True
        
        if place[y][x] == 'X' or depth == 2:
            return False
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < 5 and 0 <= ny < 5 and not visit[ny][nx]:
                result.append(find_p(depth + 1, place, visit, ny, nx))
        return any(result)
        
    
    def check_place(place: list) -> bool:
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    visit = [[False for _ in range(5)] for _ in range(5)]
                    if find_p(0, place, visit, y, x):
                        return False
        return True
        
    answer = []
    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)
                
    return answer