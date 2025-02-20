import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int max_depth = 0;
    static int[][] parent;
    static int[] depths;
    static ArrayList<Integer>[] tree;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int node1, node2;

        n = Integer.parseInt(br.readLine());
        for(int i = 1; i < n + 1; i *= 2, max_depth++);
        
        tree = new ArrayList[n + 1];
        parent = new int[max_depth][n + 1];
        depths = new int[n + 1];


        for(int i = 1; i < n + 1; i++) {
            tree[i] = new ArrayList<Integer>();
        }

        for(int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            node1 = Integer.parseInt(st.nextToken());
            node2 = Integer.parseInt(st.nextToken());

            tree[node1].add(node2);
            tree[node2].add(node1);
        }

        dfs(1, 1);
        fillParent();

        m = Integer.parseInt(br.readLine());

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            node1 = Integer.parseInt(st.nextToken());
            node2 = Integer.parseInt(st.nextToken());
            sb.append(getLca(node1, node2)).append("\n");
        }

        System.out.print(sb);

        br.close();
    }

    static void dfs(int index, int depth) {
        if(index == n + 1) {
            return;
        }

        depths[index] = depth;

        int size = tree[index].size();
        for(int i = 0; i < size; i++) {
            int childIndex = tree[index].get(i);
            if(depths[childIndex] == 0) {
                parent[0][childIndex] = index;
                dfs(childIndex, depth + 1);
            }
        }
    }

    static void fillParent() {
        for(int i = 1; i < max_depth; i++) {
            for(int j = 1; j < n + 1; j++) {
                parent[i][j] = parent[i - 1][parent[i - 1][j]];
            }
        }
    }

    static int getLca(int node1, int node2) {
        int depth1 = depths[node1];
        int depth2 = depths[node2];
        int temp;

        // node1의 깊이가 node2의 깊이보다 깊거나 같은 경우로 세팅
        if (depth1 < depth2) {
            temp = node1;
            node1 = node2;
            node2 = temp;

            temp = depth1;
            depth1 = depth2;
            depth2 = temp;
        }

        for(int i = 0, depthDiff = depth1 - depth2; depthDiff != 0; i++, depthDiff = depthDiff >> 1) {
            if((depthDiff & 1) == 0) continue;
            if((depthDiff & 1) == 1) node1 = parent[i][node1];
        }
        
        if(node1 == node2) return node1;

        for(int i = max_depth - 1; i > -1; i--) {
            if(parent[i][node1] != parent[i][node2]) {
                node1 = parent[i][node1];
                node2 = parent[i][node2];
            }
        }

        return parent[0][node1];
    }
}