#include <iostream>
#include <vector>
#include <queue>

#define INF 10e7

using namespace std;

int n, e, u, v;

vector<pair<int, int>> graph[801];

vector<int> dijkstra(int start) {
    priority_queue<pair<int, int>> pq;
    vector<int> distance(n + 1, INF);
    
    pq.push(pair<int, int>(0, start));
    distance[start] = 0;

    while(!pq.empty()) {
        int dist, node_idx;
        dist = -pq.top().first;
        node_idx = pq.top().second;
        pq.pop();

        if(distance[node_idx] < dist) continue;

        vector<pair<int, int>>::iterator iter;
        vector<pair<int, int>> node = graph[node_idx];
        for(iter = node.begin(); iter != node.end(); iter++) {
            int new_cost, cost, neighbor_idx;
            pair<int, int> neighbor = *iter;
            cost = neighbor.first;
            neighbor_idx = neighbor.second;
            new_cost = distance[node_idx] + cost;
            if(new_cost < distance[neighbor_idx]) {
                distance[neighbor_idx] = new_cost;
                pq.push(pair<int, int>(-new_cost, neighbor_idx));
            }
        }
    }

    return distance;
}

int main() {
    int route, route_u_v, route_v_u;
    vector<int> s_distance, u_distance, v_distance;

    cin >> n >> e;

    for(int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back(pair<int, int>(c, b));
        graph[b].push_back(pair<int, int>(c, a));
    }

    cin >> u >> v;

    s_distance = dijkstra(1);
    u_distance = dijkstra(u);
    v_distance = dijkstra(v);

    if(s_distance[u] == INF || u_distance[v] == INF || v_distance[n] == INF) route_u_v = INF;
    else route_u_v = s_distance[u] + u_distance[v] + v_distance[n];
    if(s_distance[v] == INF || v_distance[u] == INF || u_distance[n] == INF) route_v_u = INF;
    else route_v_u = s_distance[v] + v_distance[u] + u_distance[n];

    route = min(route_u_v, route_v_u);

    if(route == INF) cout << -1;
    else cout << route;

    return 0;
}