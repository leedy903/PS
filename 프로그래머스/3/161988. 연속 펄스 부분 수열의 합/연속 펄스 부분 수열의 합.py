def solution(sequence):
    answer = 0
    pulse = [0 for _ in range(len(sequence))]
    for i in range(len(sequence)):
        if(i % 2 == 0):
            pulse[i] = sequence[i]
        else:
            pulse[i] = -sequence[i]
    
    compress_pulse = [pulse[0]]
    for i in range(1, len(pulse)):
        if pulse[i] == 0:
            continue
        if(compress_pulse[-1] * pulse[i] < 0):
            compress_pulse.append(pulse[i])
        else:
            compress_pulse[-1] += pulse[i]
    
    if(compress_pulse[0] < 0):
        for i in range(len(compress_pulse)):
            compress_pulse[i] = -compress_pulse[i]
            
            
    positive_max = [0 for _ in range(len(compress_pulse))]
    negative_max = [0 for _ in range(len(compress_pulse))]

    positive_max[0] = compress_pulse[0]
    negative_max[0] = compress_pulse[0]
    
    if len(compress_pulse) > 1:
        positive_max[1] = compress_pulse[1]
        negative_max[1] = compress_pulse[1]
        
    for i in range(2, len(compress_pulse)):            
        if(i % 2 == 0):
            positive_max[i] = max(compress_pulse[i], positive_max[i - 2] + positive_max[i - 1] + compress_pulse[i])
            negative_max[i] = compress_pulse[i]
        if(i % 2 == 1):
            negative_max[i] = min(compress_pulse[i], negative_max[i - 2] + negative_max[i - 1] + compress_pulse[i])
            positive_max[i] = compress_pulse[i]
            
    answer = max(max(positive_max), -min(negative_max))
    
    return answer