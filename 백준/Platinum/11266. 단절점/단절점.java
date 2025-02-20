import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int v, e;
    static int order = 1;
    static int cutVertexCount = 0;
    static ArrayList<Integer>[] adjList;
    static int[] visitingOrder;
    static boolean[] isCutVertex;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        adjList = new ArrayList[v + 1];
        for(int i = 1; i < v + 1; i++) {
            adjList[i] = new ArrayList<Integer>();
        }

        int startId, targetId;
        for(int i = 1; i < e + 1; i++) {
            st = new StringTokenizer(br.readLine());
            startId = Integer.parseInt(st.nextToken());
            targetId = Integer.parseInt(st.nextToken());

            adjList[startId].add(targetId);
            adjList[targetId].add(startId);
        }

        visitingOrder = new int[v + 1];
        isCutVertex = new boolean[v + 1];

        for(int i = 1; i < v + 1; i++) {
            if(visitingOrder[i] == 0) {
                dfs(i, 0, true);
            }
        }

        for(int i = 1; i < v + 1; i++) {
            if(isCutVertex[i]) {
                cutVertexCount++;
                sb.append(i).append(" ");
            }
        }
        
        System.out.println(cutVertexCount);
        System.out.println(sb);


        br.close();

    }
    
    static int dfs(int now, int past, boolean isRoot) {
        // 방문 순서 기록
        visitingOrder[now] = order;
        order++;

        // minOrder: 함수가 return 하면서 방문했던 최소 order를 리턴
        // 역전 현상 발생 확인
        int minOrder = visitingOrder[now];
        int childCount = 0;

        // 인접 정점 모두 확인
        int size = adjList[now].size();
        for(int i = 0; i < size; i++) {
            int next = (int) adjList[now].get(i);

            // 지나온 길 다시 보지 않음
            if(next == past) continue;

            // 자식을 최초로 방문한 경우
            if(visitingOrder[next] == 0) {
                childCount++;

                // 자식 정점 중 방문순서가 가장 빠른 값
                int lowOrder = dfs(next, now, false);

                // Root가 아니고 역전이 일어나지 않으면 단절점
                if(!isRoot && lowOrder >= visitingOrder[now]) {
                    isCutVertex[now] = true;
                }
                minOrder = Math.min(minOrder, lowOrder);
            }
            // 이미 자식을 방문한 경우
            else {
                minOrder = Math.min(minOrder, visitingOrder[next]);
            }
        }

        // Root이고 자식 개수가 2개이상이면 단절점
        if(isRoot && childCount >= 2) {
            isCutVertex[now] = true;
        }
        return minOrder;
    }
}
