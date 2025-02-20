import sys
input = sys.stdin.readline

def get_max(honeypots):
    honey_sums = [honeypots[0]]
    for i in range(1, len(honeypots)):
        honey_sums.append(honey_sums[-1] + honeypots[i])

    first_bee = honey_sums[-1] - honey_sums[0]

    max_honey = 0
    for i in range(1, len(honeypots)):
        second_bee = honey_sums[-1] - honey_sums[i]
        max_honey = max(max_honey, first_bee + second_bee - honeypots[i])


    return max_honey 

n = int(input())
honeypots = list(map(int, input().split()))
if len(honeypots) == 3:
    max_honey = max(honeypots) * 2
else:
    max_honey = max(get_max(honeypots), get_max(honeypots[::-1]))
print(max_honey)