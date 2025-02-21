def solution(book_time):
    answer = 0
    books = []
    for start, end in book_time:
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        books.append([s_h * 60 + s_m, e_h * 60 + e_m])
    
    books.sort()
    
    rooms = []
    count = 0
    for start, end in books:
        for i in range(len(rooms)):
            room = rooms[i]
            if start >= room + 10:
                rooms[i] = end
                break
        else:
            rooms.append(end)    
            
    answer = len(rooms)
        
    return answer