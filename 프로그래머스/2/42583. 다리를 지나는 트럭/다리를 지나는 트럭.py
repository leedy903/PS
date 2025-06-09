def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0] * bridge_length
    weights = 0
    
    while truck_weights != []:
        
        weights -= bridge.pop(0)
        
        if weights + truck_weights[0] <= weight:
            truck_now = truck_weights.pop(0)
            bridge.append(truck_now)
            weights += truck_now
        else:
            bridge.append(0)
        
        answer += 1
    
    answer += bridge_length

            
    return answer