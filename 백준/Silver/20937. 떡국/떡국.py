from collections import Counter
N = int(input())
plates = list(map(int, input().split()))

plates = Counter(plates)
print(plates.most_common()[0][1])