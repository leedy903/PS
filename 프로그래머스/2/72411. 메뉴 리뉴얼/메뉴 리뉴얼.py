from itertools import combinations
def solution(orders, course):
    answer = []
        
    for course_size in course:
        course_cases = []
        for order in orders:
            course_cases += list(combinations(sorted(order), course_size))

        course_count = dict()
        for course_case in course_cases:
            if course_case in course_count:
                course_count[course_case] += 1
            else:
                course_count[course_case] = 1
        
        course_count = sorted(course_count.items(), key = lambda x : x[1], reverse=True)
        answer += [course for course, count in course_count if count == max(2, course_count[0][1]) ]
        
    return [''.join(course) for course in sorted(answer)]