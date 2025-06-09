def solution(sticker):
    answer = 0
    
    if len(sticker) == 1:
        answer = sticker[0]
    else:
        dp1 = [[0 for _ in range(len(sticker))] for _ in range(2)]
        for i in range(1, len(dp1[0])):
            dp1[0][i] = max(dp1[0][i - 1], dp1[1][i - 1])
            dp1[1][i] = dp1[0][i - 1] + sticker[i - 1]

        dp2 = [[0 for _ in range(len(sticker))] for _ in range(2)]
        for i in range(1, len(dp2[0])):
            dp2[0][i] = max(dp2[0][i - 1], dp2[1][i - 1])
            dp2[1][i] = dp2[0][i - 1] + sticker[i]

        answer = max(max(map(max, dp1)), max(map(max, dp2)))
    
    return answer