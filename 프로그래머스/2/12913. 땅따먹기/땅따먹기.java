import java.util.*;
import java.io.*;

class Solution {
    int solution(int[][] land) {
        int answer = 0;
        int[][] dp = new int[land.length + 1][4];
        for (int i = 1; i < dp.length; i++) {
            for (int j = 0; j < 4; j++) {
                int max = Integer.MIN_VALUE;
                for (int k = 0; k < 4; k++) {
                    if (j == k) continue;
                    max = Math.max(max, dp[i - 1][k]);
                }
                dp[i][j] = max + land[i - 1][j];
            }
        }

        for (int i = 0; i < 4; i++) {
            answer = Math.max(answer, dp[land.length][i]);
        }
        
        return answer;
    }
}