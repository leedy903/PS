import sys
input = sys.stdin.readline

correct = "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"

answer = 64
N, M = map(int, input().strip().split())
board = [list(input().strip()) for _ in range(N)]

for y in range(N - 7):
    for x in range(M - 7):
        wrong_1 = 0
        wrong_2 = 0
        for i in range(64):
            y_offset = i // 8
            x_offset = i % 8
            horse = board[y + y_offset][x + x_offset]
            if horse == correct[i]:
                wrong_1 += 1
            if horse != correct[i]:
                wrong_2 += 1
        answer = min(answer, min(wrong_1, wrong_2))

print(answer)