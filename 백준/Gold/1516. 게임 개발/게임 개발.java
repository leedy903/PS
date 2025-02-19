import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] indegree;
    static int[] buildTimes;
    static ArrayList<Integer>[] startEdgeList;
    static ArrayList<Integer>[] targetEdgeList;
    static ArrayDeque<Integer> queue;
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());

        indegree = new int[n + 1];
        buildTimes = new int[n + 1];
        startEdgeList = new ArrayList[n + 1];
        targetEdgeList = new ArrayList[n + 1];
        queue = new ArrayDeque<>();

        for(int i = 1; i < n + 1; i++) {
            startEdgeList[i] = new ArrayList<Integer>();
            targetEdgeList[i] = new ArrayList<Integer>();
        }

        for(int targetId = 1; targetId < n + 1; targetId++) {
            st = new StringTokenizer(br.readLine());
            int buildTime = Integer.parseInt(st.nextToken());
            buildTimes[targetId] = buildTime;

            int startId = Integer.parseInt(st.nextToken());
            while(startId != -1) {
                startEdgeList[startId].add(targetId);
                targetEdgeList[targetId].add(startId);
                indegree[targetId]++;
                startId = Integer.parseInt(st.nextToken());
            } 
        }

        for(int startId = 1; startId < n + 1; startId++) {
            if(indegree[startId] == 0) queue.offer(startId);
        }

        while(!queue.isEmpty()) {
            int size;
            int startId = queue.poll();
            int buildTime = buildTimes[startId];
            int maxWaitingTime = 0;

            size = targetEdgeList[startId].size();
            for(int i = 0; i < size; i++) {
                int preBuildId = (int)targetEdgeList[startId].get(i);
                maxWaitingTime = Math.max(maxWaitingTime, buildTimes[preBuildId]);
            }

            buildTime += maxWaitingTime;
            buildTimes[startId] = buildTime;

            size = startEdgeList[startId].size();
            for(int i = 0; i < size; i++) {
                int targetId = (int)startEdgeList[startId].get(i);
                indegree[targetId]--;
                
                if(indegree[targetId] == 0) queue.offer(targetId);
            }
        }

        for(int i = 1; i < n + 1; i++) {
            sb.append(buildTimes[i]).append("\n");
        }
    
        System.out.println(sb);
        br.close();
    }
}


