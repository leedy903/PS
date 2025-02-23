def solution(survey, choices):

    survey_result = {"TR" : 0, "FC" : 0, "MJ" : 0, "NA" : 0}
    
    for question_type, score in zip(survey, choices):
        if question_type not in survey_result.keys():
            question_type = question_type[::-1]
            survey_result[question_type] -= score - 4
        else:
            survey_result[question_type] += score - 4

    answer = ""
    for _type in survey_result.keys():
        if survey_result[_type] >= 0:
            answer += _type[1]
        else:
            answer += _type[0]
        
    return answer