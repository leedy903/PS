import java.io.*;
import java.util.*;

class Edge {
    int startId, targetId, cost;

    public Edge(int startId, int targetId, int cost) {
        this.startId = startId;
        this.targetId = targetId;
        this.cost = cost;
    }
}

public class Main {
    static int n, m;
    static boolean hasNegativeCycle = false;
    static final int INF = (int) 1e9;
    static final int start = 1;
    static long[] dist;
    static Edge[] edgeList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dist = new long[n + 1];
        edgeList = new Edge[m];

        Arrays.fill(dist, INF);
        dist[start] = 0;

        int startId, targetId, cost;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            startId = Integer.parseInt(st.nextToken());
            targetId = Integer.parseInt(st.nextToken());
            cost = Integer.parseInt(st.nextToken());
            edgeList[i] = new Edge(startId, targetId, cost);
        }

        bellmanFord(start);

        if (hasNegativeCycle == true) {
            sb.append("-1\n");
        }
        else {
            for (int i = 2; i < n + 1; i++) {
                if (dist[i] != INF) {
                    sb.append(dist[i]).append("\n");
                }
                else {
                    sb.append("-1\n");
                }
            }
        }

        System.out.print(sb);
        br.close();
    }

    static void bellmanFord(int start) {
        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < m; j++) {
                Edge now = edgeList[j];
                if (dist[now.startId] == INF) continue;
                if (dist[now.targetId] > dist[now.startId] + now.cost) {
                    dist[now.targetId] = dist[now.startId] + now.cost;
                    if (i == n) {
                        hasNegativeCycle = true;
                    }
                }
            }
        }
        return;
    }
}