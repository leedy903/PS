# 가능한 모든 할인율의 경우의 수를 담을 배열
discount_rates_cases = []

def solution(users, emoticons):
    answer = [0, 0]
    
    # 가능한 모든 할인율의 경우의 수를 계산
    dfs(0, [0 for _ in range(len(emoticons))])
    
    # 가능한 모든 할인율의 경우의 수를 순회
    for discount_rates in discount_rates_cases:
        # 이모티콘 플러스 숫자
        emoticon_plus = 0
        # 매출액
        profit = 0
        # 유저별 이모티콘 플러스 가입 여부 및 매출액 확인
        for user_rate, user_limit in users:
            payment = 0
            # 유저가 구매할 이모티콘 계산
            for j, discount_rate in enumerate(discount_rates):
                # 유저가 원하는 할인율 보다 크다면 구매
                if user_rate <= discount_rate:
                    payment += emoticons[j] * ((100 - discount_rate) / 100)
            # 유저가 이모티콘 플러스를 가입할 지 구매할 지 결정
            if payment >= user_limit:
                emoticon_plus += 1
            else:
                profit += payment

        # 1. 이모티콘 플러스 서비스 가입자 최대한 늘리기
        # 2. 이모티콘 매출액 최대한 늘리기
        if answer[0] < emoticon_plus:
            answer = [emoticon_plus, profit]
        elif answer[0] == emoticon_plus:
            if answer[1] < profit:
                answer = [emoticon_plus, profit]
        
    return answer
        
# 가능한 discount 조합 모두 구하기
def dfs(depth, discount_rates):
    if depth == len(discount_rates):
        discount_rates_cases.append(discount_rates[:])
        return

    # 10부터 40까지 할인율 하나씩 추가
    for discount_rate in range(10, 50, 10):
        discount_rates[depth] += discount_rate
        dfs(depth + 1, discount_rates)
        discount_rates[depth] -= discount_rate
