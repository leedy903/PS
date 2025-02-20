import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
city = [[] for _ in range(N)]

houses = []
restaurants = []
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    city.append(data)
    for j in range(N):
        if data[j] == 1:
            houses.append([i, j])
        elif data[j] == 2:
            restaurants.append([i, j])

min_city_chicken_distance = int(1e9)
restaurant_case = combinations(restaurants, M)
for r_case in restaurant_case:
    city_chicken_distance = 0
    for house in houses:
        hy, hx = house
        min_chicken_distance = int(1e9)
        for restaurant in r_case:
            ry, rx = restaurant
            chicken_distance = abs(ry - hy) + abs(rx - hx)
            min_chicken_distance = min(chicken_distance, min_chicken_distance)
        city_chicken_distance += min_chicken_distance
    min_city_chicken_distance = min(city_chicken_distance, min_city_chicken_distance)

print(min_city_chicken_distance)