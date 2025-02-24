import java.util.*;

class Solution {
    static boolean[] visited;
    static int[][] networks;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        networks = new int[n][n];
        
        Arrays.fill(visited, false);
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                networks[i][j] = computers[i][j];
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                dfs(i);
            }
        }
        
        return answer;
    }
    
    public void dfs(int node) {
        visited[node] = true;
        for (int i = 0; i < networks.length; i++) {
            if (networks[node][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }
}