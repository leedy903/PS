import sys

def direction_list(init_d: int, g: int) -> list:
    directions = [init_d]
    for _ in range(g):
        temp_list = directions[:]
        while temp_list:
            directions.append((temp_list.pop() + 1) % 4)
    return directions

def dragon_curves(x: int, y: int, init_d: int, g: int) -> None:
    _direction_list = direction_list(init_d, g)
    _map[y][x] = 1
    for direction in _direction_list:
        x = dx[direction] + x
        y = dy[direction] + y
        _map[y][x] = 1

def square_count() -> int:
    count = 0
    for i in range(map_size - 1):
        for j in range(map_size - 1):
            if _map[j][i] == 1 and _map[j+1][i] == 1 and _map[j][i+1] == 1 and _map[j+1][i+1] == 1:
                count += 1
    return count

if __name__ == "__main__":
    # Set Map
    map_size = 101
    _map = [[0 for _ in range(map_size)] for _ in range(map_size)]

    # Set direction
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # Get input
    N = int(sys.stdin.readline())

    curve_infos = [[] for _ in range(N)]

    for i in range(N):
        curve_infos[i] = list(map(int, sys.stdin.readline().split()))
    
    for i in range(N):
        dragon_curves(*curve_infos[i])  

    print(square_count())