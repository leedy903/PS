def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        row = bin(num1 | num2)[2:]
        row = row.replace("1", "#")
        row = row.replace("0", " ")
        left_space = " " * (n - len(row))
        answer.append(left_space + row)
    return answer