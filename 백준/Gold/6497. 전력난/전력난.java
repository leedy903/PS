import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge> {

    int x;
    int y;
    int z;

    public Edge (int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public int compareTo(Edge e) {
        if (this.z > e.z) return 1;
        else return -1;
    }

}

public class Main {
    static int m, n;
    static int edgeCount, totalCost, saveCost;
    static PriorityQueue<Edge> pq;
    static int[] parents;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());

            edgeCount = 0;
            totalCost = 0;
            saveCost = 0;

            if (m == 0 && n == 0) {
                break;
            }

            parents = new int[m + 1];
            pq = new PriorityQueue<>();

            for (int i = 0; i < m + 1; i++) {
                parents[i] = i;
            }

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int z = Integer.parseInt(st.nextToken());
                totalCost += z;
                pq.offer(new Edge(x, y, z));
            }

            while (!pq.isEmpty() && edgeCount < m) {
                Edge edge = pq.poll();

                if (find(edge.x) == find(edge.y)) continue;

                union(edge.x, edge.y);
                edgeCount++;
                saveCost += edge.z;

            }

            sb.append(totalCost - saveCost).append("\n");
        }

        System.out.print(sb);

        br.close();
    }

    public static int find(int x) {
        if (x != parents[x]) {
            x = find(parents[x]);
        }
        return parents[x];
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x < y) parents[y] = x;
        else parents[x] = y;

        return;
    }
}