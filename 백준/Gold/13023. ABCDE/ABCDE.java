import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static Boolean isExist = false;
    static HashMap<Integer, ArrayList<Integer>> relationships = new HashMap<Integer, ArrayList<Integer>>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int a, b;
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            ArrayList<Integer> friends;
            if(!relationships.containsKey(a)) {
                friends = new ArrayList<Integer>();
            }
            else {
                friends = relationships.get(a);
            }
            friends.add(b);
            relationships.put(a, friends);

            if(!relationships.containsKey(b)) {
                friends = new ArrayList<Integer>();
            }
            else {
                friends = relationships.get(b);
            }
            friends.add(a);
            relationships.put(b, friends);
        }

        Boolean[] visited = new Boolean[n];
        Arrays.fill(visited, false);

        relationships.forEach((start, friends) -> {
            visited[start] = true;
            dfs(1, start, visited);
            visited[start] = false;
        });

        if(isExist) System.out.println(1);
        else System.out.println(0);

        br.close();
    }
    

    public static void dfs(int depth, int cur_node, Boolean[] visited) {

        if(isExist) return;

        if(depth == 5) {
            isExist = true;
            return;
        }

        ArrayList<Integer> friends = relationships.get(cur_node);
        for(int next_node : friends) {
            if(visited[next_node] == false) {
                visited[next_node] = true;
                dfs(depth + 1, next_node, visited);
                visited[next_node] = false;
            }
        }
    }
}