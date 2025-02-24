edges = {}
airports_id = {}
num_airports = 0
num_tickets = 0
answer = []

def solution(tickets):
    global edges, airports_id, num_airports, num_tickets, answer
    
    tickets.sort(key = lambda x : (x[0], x[1]))
    num_tickets = len(tickets)
    
    
    for departure, arrival in tickets:
        if departure not in edges:
            edges[departure] = []
        edges[departure].append(arrival)
        
        if arrival not in edges:
            edges[arrival] = []
    
    airports = set()
    
    for departure, arrival in tickets:
        airports.add(departure)
        airports.add(arrival)
    
    airports = sorted(airports)
    
    num_airports = len(airports)
    
    for i in range(len(airports)):
        airports_id[airports[i]] = i
    
    visited = [[0 for _ in range(num_airports)] for _ in range(num_airports)]
    for departure, arrival in tickets:
        departure_id, arrival_id = airports_id[departure], airports_id[arrival]
        visited[departure_id][arrival_id] += 1
    
    dfs(0, "ICN", ["ICN"], visited)
    
    return answer

def dfs(depth, departure, path, visited):
    global edges, airports_id, num_airports, num_tickets, answer
    
    if sum(map(sum, visited)) == 0:
        if len(answer) == 0:
            answer = path[:]
        return
    
    for arrival in edges[departure]:
        departure_id, arrival_id = airports_id[departure], airports_id[arrival]
        
        if visited[departure_id][arrival_id] > 0:
            visited[departure_id][arrival_id] -= 1
            path.append(arrival)
            dfs(depth + 1, arrival, path, visited)
            visited[departure_id][arrival_id] += 1
            path.pop()