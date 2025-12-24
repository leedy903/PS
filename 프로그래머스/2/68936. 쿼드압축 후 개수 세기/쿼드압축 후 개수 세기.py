def solution(arr):
    answer = [0, 0]
    dy = [0, 0, 1, 1]
    dx = [0, 1, 0, 1]
    def compression(y, x, w):
        total = sum(sum(row[x:x+w]) for row in arr[y:y+w])
        
        if total == 0:
            return [1, 0]
        if total == w * w:
            return [0, 1]
        
        half = w // 2
        zero, one = 0, 0
        for i in range(4):
            z, o = compression(y + dy[i] * half, x + dx[i] * half, half)
            zero += z
            one += o
        return [zero, one]
        
    return compression(0, 0, len(arr))