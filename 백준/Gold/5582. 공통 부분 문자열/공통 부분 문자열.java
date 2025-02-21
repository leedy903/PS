import java.io.*;
import java.util.*;

public class Main {
    static String sequence1;
    static String sequence2;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        sequence1 = br.readLine();
        sequence2 = br.readLine();

        int n = sequence1.length();
        int m = sequence2.length();
        
        dp = new int[n + 1][m + 1];
        
        int lcsLength = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (sequence1.charAt(i - 1) == sequence2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    lcsLength = Math.max(dp[i][j], lcsLength);
                }
            }
        }
        
        System.out.println(lcsLength);

        br.close();
    }
}