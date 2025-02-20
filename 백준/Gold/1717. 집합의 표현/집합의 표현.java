import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] parent;
    static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        for(int i = 0; i < n + 1; i++) {
            parent[i] = i;
        }

        int op, a, b;
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            op = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            if(op == 0) union(a, b);
            else {
                a = find(a);
                b = find(b);
                if(a == b) sb.append("YES").append("\n");
                else sb.append("NO").append("\n");
            }

        }

        System.out.print(sb);

        br.close();
    }

    public static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a < b) parent[a] = b;
        else parent[b] = a;

    }

    public static int find(int x) {
        if(x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
}
