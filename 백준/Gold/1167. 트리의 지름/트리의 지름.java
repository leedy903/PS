import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

class Point {
    int node;
    int cost;
    Point (int node, int cost) {
        this.node = node;
        this.cost = cost;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int V = Integer.parseInt(br.readLine());

        List<Point>[] graph = new ArrayList[V];

        for (int i = 0; i < V; i++) {
            graph[i] = new ArrayList<Point>();
        }

        for (int i = 0; i < V; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            while (true) {
                int v = Integer.parseInt(st.nextToken());
                if (v == -1) {
                    break;
                }
                int c = Integer.parseInt(st.nextToken());
                graph[u - 1].add(new Point(v - 1, c));
            }
        }

        int[] dist = new int[V];
        boolean[] visited = new boolean[V];
        Deque<Integer> deq = new ArrayDeque<>();

        Arrays.fill(dist, 0);
        Arrays.fill(visited, false);

        visited[0] = true;
        deq.offer(0);

        while(!deq.isEmpty()) {
            int cur = deq.poll();
            for (Point next : graph[cur]) {
                if (!visited[next.node]) {
                    dist[next.node] = dist[cur] + next.cost;
                    visited[next.node] = true;
                    deq.offer(next.node);
                }
            }
        }

        int maxIdx = -1, maxCost = -1;
        for (int i = 0; i < V; i++) {
            if (maxCost < dist[i]) {
                maxCost = dist[i];
                maxIdx = i;
            }
        }

        dist = new int[V];
        visited = new boolean[V];
        deq = new ArrayDeque<>();

        Arrays.fill(dist, 0);
        Arrays.fill(visited, false);

        visited[maxIdx] = true;
        deq.offer(maxIdx);

        while(!deq.isEmpty()) {
            int cur = deq.poll();
            for (Point next : graph[cur]) {
                if (!visited[next.node]) {
                    dist[next.node] = dist[cur] + next.cost;
                    visited[next.node] = true;
                    deq.offer(next.node);
                }
            }
        }

        maxCost = -1;
        for (int i = 0; i < V; i++) {
            maxCost = Math.max(maxCost, dist[i]);
        }

        System.out.println(maxCost);

        br.close();
    }
}
