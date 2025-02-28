import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int index;
    int weight;
    Node(int index, int weight) {
        this.index = index;
        this.weight = weight;
    }

    @Override
    public int compareTo(Node n) {
        if (this.weight > n.weight) return 1;
        else return -1;
    }
}

public class Main {
    static int n, m, s, d;
    static int[] dist;
    static List<Node>[] graph;
    static List<Integer>[] route;
    static boolean[][] shortestPath;
    static final int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            if (n == 0 && m == 0) break;

            dist = new int[n];
            graph = new ArrayList[n];
            route = new ArrayList[n];
            shortestPath = new boolean[n][n];

            for (int i = 0; i < n; i++) {
                graph[i] = new ArrayList<Node>();
                route[i] = new ArrayList<Integer>();
                Arrays.fill(shortestPath[i], false);
            }

            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());

            int u, v, w;
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                u = Integer.parseInt(st.nextToken());
                v = Integer.parseInt(st.nextToken());
                w = Integer.parseInt(st.nextToken());
                graph[u].add(new Node(v, w));
            }

            dijkstra(s);
            removeDfs(d);
            dijkstra(s);
            if (dist[d] == INF) {
                sb.append(-1).append("\n");
            }
            else {
                sb.append(dist[d]).append("\n");
            }

        }
        System.out.print(sb);
        br.close();
    }

    public static void dijkstra(int start) {
        Arrays.fill(dist, INF);
        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.offer(new Node(start, 0));
        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (dist[now.index] < now.weight) continue;
            int size = graph[now.index].size();
            for (int i = 0; i < size; i++) {
                Node next = graph[now.index].get(i);
                if (shortestPath[now.index][next.index] == true) continue;
                int cost = dist[now.index] + next.weight;
                if (dist[next.index] > cost) {
                    dist[next.index] = cost;
                    route[next.index] = new ArrayList<>();
                    route[next.index].add(now.index);
                    pq.offer(new Node(next.index, cost));
                }
                else if (dist[next.index] == cost) {
                    route[next.index].add(now.index);
                }
            }
        }
    }

    public static void removeDfs(int now) {
        if (now == s) return;

        int size = route[now].size();
        for (int i = 0; i < size; i++) {
            int before = route[now].get(i);
            if (!shortestPath[before][now])  {
                shortestPath[before][now] = true;
                removeDfs(before);
            }
        }

    }
}