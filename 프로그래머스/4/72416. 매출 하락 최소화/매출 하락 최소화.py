from collections import defaultdict

def solution(sales, links):
    answer = 0
    n = len(sales) + 1
    tree = defaultdict(list)
    
    for parent, child in links:
        tree[parent].append(child)
    
    dp = [[0, 0] for _ in range(n)]
    
    def dfs(cur_node):
        if not tree[cur_node]:
            dp[cur_node][1] = sales[cur_node - 1]
            return
        
        base = 0
        best_extra = float('inf')
        
        for child in tree[cur_node]:
            dfs(child)
            m = min(dp[child][0], dp[child][1])
            base += m
            best_extra = min(best_extra, dp[child][1] - m)
        
        dp[cur_node][0] = base + best_extra
        dp[cur_node][1] = sales[cur_node - 1] + base
    
    dfs(1)
    answer = min(dp[1][0], dp[1][1])
    
    return answer