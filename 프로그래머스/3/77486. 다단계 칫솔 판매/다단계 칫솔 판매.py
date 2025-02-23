def solution(enroll, referral, seller, amount):
    answer = []
    
    N = len(enroll)
    enroll_graph = {enroll[i] : referral[i] for i in range(N)}
    total_income = {enroll[i] : 0 for i in range(N)}
    
    for _seller, _amount in zip(seller, amount):
        
        income = _amount * 100
        total_income[_seller] += income - income // 10
        next_seller = enroll_graph[_seller]
        
        while next_seller != "-" and income != 0:
            income //= 10
            total_income[next_seller] += income - income // 10
            next_seller = enroll_graph[next_seller]
            
    answer = list(total_income.values())
    
    return answer

    
