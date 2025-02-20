n = int(input())
sequence = [int(input()) for _ in range(n)]
sequence = [0] + sequence

candidate_values = []
candidate_indexes = []
def dfs(idx, indexes, values):
    global candidate_indexes, candidate_values
    now = sequence[idx]

    if now in values:
        candidate_indexes = indexes
        candidate_values = values
        return;

    indexes.append(idx)
    values.append(now)
    dfs(now, indexes, values)

answer = set()
for i in range(1, len(sequence)):
    dfs(i, [], [])
    candidate_indexes.sort()
    candidate_values.sort()
    if candidate_indexes == candidate_values:
        for v in candidate_values:
            answer.add(v)


answer = sorted(answer)
print(len(answer))
for a in answer:
    print(a)