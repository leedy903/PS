import math
def solution(fees, records):
    answer = []
    MAX = 9999
    last_time = "23:59"
    
    entry_time_records = [""] * MAX
    parking_time_records = [0] * MAX
    
    min_time, min_fee, unit_time, unit_fee = fees
    
    for record in records:
        time, car_id, state = record.split()
        if state == 'IN':
            entry_time_records[int(car_id)] = time
        elif state == 'OUT':
            entry_time = entry_time_records[int(car_id)]
            entry_h, entry_m = map(int, entry_time.split(":"))
            out_h, out_m = map(int, time.split(":"))
            parking_time = (out_h * 60 + out_m) - (entry_h * 60 + entry_m)
            parking_time_records[int(car_id)] += parking_time
            entry_time_records[int(car_id)] = ""
            
    for car_id, entry_time in enumerate(entry_time_records):
        if entry_time != "":
            entry_h, entry_m = map(int, entry_time.split(":"))
            out_h, out_m = map(int, last_time.split(":"))
            parking_time = (out_h * 60 + out_m) - (entry_h * 60 + entry_m)
            parking_time_records[int(car_id)] += parking_time
            entry_time_records[int(car_id)] = ""
    
    for parking_time in parking_time_records:
        if parking_time != 0:
            if parking_time > min_time:
                extra_parking_time = parking_time - min_time
                total_fee = math.ceil(extra_parking_time/unit_time) * unit_fee + min_fee
            else:
                total_fee = min_fee
            answer.append(total_fee)
        
    return answer