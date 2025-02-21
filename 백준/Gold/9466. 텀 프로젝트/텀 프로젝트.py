T = int(input())

answer = ""
for t in range(T):
    n = int(input())
    student_id = [0] + list(map(int, input().split()))
    visited = [True] + [False for _ in range(n)]

    has_team = 0
    for i, s_id in enumerate(student_id):
        cycle = []
        current = i
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = student_id[current]

        if current in cycle:
            has_team += len(cycle[cycle.index(current):])
    answer += str(n - has_team) + "\n"

print(answer)