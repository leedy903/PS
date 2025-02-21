from heapq import heappop, heappush
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answers = []
dps = []
while True:
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    loss_matrix = [[float('inf') for  _ in range(n)] for _ in range(n)]
    loss_matrix[0][0] = matrix[0][0]
    heap = []
    heappush(heap, (loss_matrix[0][0], [0, 0]))
    while heap:
        loss, position = heappop(heap)
        y, x  = position
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                next_loss = matrix[ny][nx] + loss
                if next_loss < loss_matrix[ny][nx]:
                    loss_matrix[ny][nx] = next_loss
                    heappush(heap, (loss_matrix[ny][nx], [ny, nx]))
    answers.append(loss_matrix[n - 1][n - 1])
for i in range(len(answers)):
    print(f"Problem {i + 1}: {answers[i]}")