import java.util.*;
class Solution {
    public static int[][] dp;
    public int solution(int m, int n, int[][] puddles) {
        dp = new int[n + 1][m + 1];
        for(int i = 0; i < n + 1; i++) {
            Arrays.fill(dp[i], 0);
        }
        
        dp[1][1] = 1;
        for(int i = 0; i < puddles.length; i++) {
            dp[puddles[i][1]][puddles[i][0]] = -1;
        }
        
        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < m + 1; j++) {
                if(i == 1 && j == 1) continue;
                if(dp[i][j] == -1) dp[i][j] = 0;
                else dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1_000_000_007;
            }
        }
        
        return dp[n][m];
    }
}