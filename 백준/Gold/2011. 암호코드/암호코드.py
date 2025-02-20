code_num = input()

code_length = len(code_num)
count = [0 for _ in range(code_length + 1)]

if int(code_num[0]) == 0:
    print(0)
else:
    code_num = '0' + code_num
    count[0] = count[1] = 1
    for i in range(2, code_length + 1):
        if int(code_num[i]) > 0:
            count[i] += count[i - 1]
        if 10 <= int(code_num[i - 1: i + 1]) < 27:
            count[i] += count[i - 2]
    print(count[code_length]%1000000)