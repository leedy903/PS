import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge>{
    int v1, v2;
    int cost;
    
    public Edge(int v1, int v2, int cost) {
        this.v1 = v1;
        this.v2 = v2;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge e) {
        if(this.cost > e.cost) {
            return 1;
        }
        else return -1;
    }

}

public class Main {
    static int n, m;
    static int totalCost, edgeCount;
    static int [] parent;
    static PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        parent = new int[n + 1];
        for(int i = 0; i < n + 1; i++) {
            parent[i] = i;
        }
    
        int a, b, c;

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            Edge edge = new Edge(a, b, c);
            pq.offer(edge);
        }

        while(!pq.isEmpty()) {
            if(edgeCount == n - 1) break;

            Edge edge = pq.poll();

            if(find(edge.v1) == find(edge.v2)) continue;
            
            union(edge.v1, edge.v2);

            edgeCount++;
            totalCost += edge.cost;
        }

        System.out.println(totalCost);

        br.close();        
    }

    public static void union(int c1, int c2) {
        c1 = parent[c1];
        c2 = parent[c2];

        if(c1 < c2) parent[c2] = c1;
        else parent[c1] = c2;

        return;
    }

    public static int find(int c) {
        if(c != parent[c]) {
            parent[c] = find(parent[c]);
        }
        return parent[c];
    }


}
