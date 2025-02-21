import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] indegree;
    static ArrayList<Integer>[] edgeList;
    static ArrayDeque<Integer> queue;
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        sb = new StringBuilder();
        
        indegree = new int[n + 1];
        edgeList = new ArrayList[n + 1];
        
        for(int i = 1; i < n + 1; i++) {
            edgeList[i] = new ArrayList<Integer>();
        }
        
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int startId = Integer.parseInt(st.nextToken());
            int targetId = Integer.parseInt(st.nextToken());

            edgeList[startId].add(targetId);
            indegree[targetId]++;
        }

        queue = new ArrayDeque<>();
        for(int i = 1; i < n + 1; i++) {
            if(indegree[i] == 0) queue.offer(i);
        }

        while(!queue.isEmpty()) {
            int startId = queue.poll();
            sb.append(startId).append(" ");

            int size = edgeList[startId].size();
            for(int i = 0; i < size; i++) {
                int targetId = (int) edgeList[startId].get(i);
                indegree[targetId]--;
                if(indegree[targetId] == 0) queue.add(targetId);
            }
        }

        System.out.println(sb);
        br.close();
    }
}
