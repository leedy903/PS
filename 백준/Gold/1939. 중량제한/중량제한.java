import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
    int start;
    int end;
    int cost;

    public Node(int start, int end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return Integer.compare(o.cost, this.cost);
    }
}

public class Main {
    public static int N, M;
    public static List<Node> edges;
    public static int[] parents;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int f1, f2, answer = -1;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        edges = new ArrayList<>();
        parents = new int[N + 1];

        for (int i = 0; i <= N; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            edges.add(new Node(u, v, w));
        }

        st = new StringTokenizer(br.readLine());
        f1 = Integer.parseInt(st.nextToken());
        f2 = Integer.parseInt(st.nextToken());

        Collections.sort(edges);

        for (int i = 0; i < M; i++) {
            Node node = edges.get(i);
            if (find(node.start) != find(node.end)) {
                union(node.start, node.end);
            }

            if (find(f1) == find(f2)) {
                answer = node.cost;
                break;
            }
        }

        System.out.println(answer);

        br.close();
    }

    public static int find(int node) {
        if (node != parents[node]) {
            node = find(parents[node]);
        }
        return  parents[node];
    }

    public static void union(int a, int b) {
        a = find(a);
        b = find(b);

        if (a > b) parents[b] = a;
        else parents[a] = b;
    }
}