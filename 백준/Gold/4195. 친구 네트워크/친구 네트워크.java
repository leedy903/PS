import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    static int t, f;
    static int[] parent;
    static int[] count;
    static HashMap<String, Integer> nameId;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        t = Integer.parseInt(br.readLine());
        for(int test_case = 0; test_case < t; test_case++) {
            f = Integer.parseInt(br.readLine());

            nameId = new HashMap<String, Integer>();

            parent = new int[f * 2 + 1];
            count = new int[f * 2 + 1];

            for(int i = 0; i < f * 2 + 1; i++) {
                parent[i] = i;
                count[i] = 1;
            }

            for(int i = 0; i < f; i++) {
                String[] relationship = br.readLine().split(" ");
                String friend1 = relationship[0];
                String friend2 = relationship[1];

                if(!nameId.containsKey(friend1)) {
                    nameId.put(friend1, nameId.size() + 1);
                }
                if(!nameId.containsKey(friend2)) {
                    nameId.put(friend2, nameId.size() + 1);
                }

                int id1 = nameId.get(friend1);
                int id2 = nameId.get(friend2);

                union(id1, id2);

                sb.append(count[find(id1)]).append("\n");

            }
        }

        System.out.print(sb);
        br.close();
    }

    public static int find(int x) {
        if(x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public static void union(int a, int b) {
        a = find(a);
        b = find(b);

        if(a < b) {
            parent[b] = a;
            count[a] += count[b];
        }
        else if(a > b) {
            parent[a] = b;
            count[b] += count[a];
        }
    }
}