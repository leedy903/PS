import java.util.*;
import java.io.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] graph = new int[n + 1][n + 1];
        
        for (int i = 0; i < n + 1; i++) {
            Arrays.fill(graph[i], 0);
        }
        
        
        for (int i = 0; i < results.length; i++) {
            int win = results[i][0];
            int lose = results[i][1];
            graph[win][lose] = 1;
        }
        
        for (int k = 0; k < n + 1; k++) {
            for (int i = 0; i < n + 1; i++) {
                for (int j = 0; j < n + 1; j++) {
                    if (graph[i][k] == 1 && graph[k][j] == 1) {
                        graph[i][j] = 1;
                    }
                }
            }
        }
        
        for (int i = 1; i < n + 1; i++) {
            int game = 0;
            for (int j = 1; j < n + 1; j++) {
                if (graph[i][j] == 1 || graph[j][i] == 1) {
                    game++;
                } 
            }
            if (game == n - 1) {
                answer++;
            }
        }
        
        
        return answer;
    }
}