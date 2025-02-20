N = int(input())
Distance = list(map(int, input().split()))
Cost = list(map(int, input().split()))
t_cost = 0
m_cost = Cost[0]
for i in range(len(Distance)):
    if Cost[i] < m_cost:
        m_cost = Cost[i]
    t_cost += m_cost*Distance[i]
print(t_cost)