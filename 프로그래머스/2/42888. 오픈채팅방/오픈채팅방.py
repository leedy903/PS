def solution(record):
    answer = []
    user_enterlist = []
    nickname_by_uid = {}
    for transaction in record:
        transaction = transaction.split()
        command, uid = transaction[0], transaction[1]
        if command == 'Enter':
            nickname_by_uid[uid] = transaction[2]
            user_enterlist.append([uid, "님이 들어왔습니다."])
        elif command == 'Leave':
            user_enterlist.append([uid, "님이 나갔습니다."])
        elif command == 'Change':
            nickname_by_uid[uid] = transaction[2]
            
    for (uid, message) in user_enterlist:
        answer.append(nickname_by_uid[uid] + message)
        
    return answer