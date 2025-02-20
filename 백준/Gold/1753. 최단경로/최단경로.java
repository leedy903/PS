import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int index;
    long weight;
    Node(int index, long cost) {
        this.index = index;
        this.weight = cost;
    }

    @Override
    public int compareTo(Node e) {
        if (this.weight > e.weight) return 1;
        else return -1;
    }
}

public class Main {
    static int v, e, k;
    static long[] dist;
    static List<Node>[] graph;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(br.readLine());

        dist = new long[v + 1];
        graph = new ArrayList[v + 1];

        Arrays.fill(dist, INF);
        for (int i = 0; i < v + 1; i++) {
            graph[i] = new ArrayList<Node>();
        }

        int nodeFrom, nodeTo;
        long weight;
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            nodeFrom = Integer.parseInt(st.nextToken());
            nodeTo = Integer.parseInt(st.nextToken());
            weight = Long.parseLong(st.nextToken());
            graph[nodeFrom].add(new Node(nodeTo, weight));
        }

        dijkstra(k);
        for (int i = 1; i < v + 1; i++) {
            if (dist[i] != INF) {
                sb.append(dist[i]).append("\n");
            }
            else {
                sb.append("INF\n");
            }
        }
        System.out.print(sb);
        br.close();
    }
    public static void dijkstra(int start) {
        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.offer(new Node(start, 0));
        while(!pq.isEmpty()) {
            Node now = pq.poll();
            if (dist[now.index] < now.weight) {
                continue;
            }
            int size = graph[now.index].size();
            for (int i = 0; i < size; i++) {
                Node next = graph[now.index].get(i);
                long cost = dist[now.index] + next.weight;
                if (dist[next.index] > cost) {
                    dist[next.index] = cost;
                    pq.offer(new Node(next.index, cost));
                }
            }
        }
    }
}
