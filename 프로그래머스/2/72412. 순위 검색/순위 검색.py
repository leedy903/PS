def solution(info, query):
    answer = []

    every_case = dict()
    for lang in ['cpp', 'java', 'python', '-']:
        for depart in ['backend', 'frontend', '-']:
            for career in ['junior', 'senior', '-']:
                for soulfood in ['chicken', 'pizza', '-']:
                    case = lang + depart + career + soulfood
                    every_case[case] = []

    for row in info:
        row = row.split()
        for lang in [row[0], '-']:
            for depart in [row[1], '-']:
                for career in [row[2], '-']:
                    for soulfood in [row[3], '-']:
                        case = lang + depart + career + soulfood
                        every_case[case].append(int(row[4]))

    for case in every_case.keys():
        every_case[case].sort()

    for conditions in query:
        conditions = conditions.replace(' and ', '')
        conditions = conditions.split()

        score_condition = int(conditions[1])
        conditions = conditions[0]

        scores = every_case[conditions]

        length = len(scores) 
        index = 0

        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if scores[mid] < score_condition:
                left = mid + 1
            else:
                right = mid - 1

        index = left

        answer.append(length - index)

    return answer