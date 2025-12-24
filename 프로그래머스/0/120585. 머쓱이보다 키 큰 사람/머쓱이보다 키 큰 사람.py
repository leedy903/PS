def solution(array, height):
    array.sort()
    for i in range(len(array)):
        if height < array[i]:
            return len(array) - i
    return 0