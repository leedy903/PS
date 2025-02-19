import java.io.*;
import java.util.*;

public class Main {
    static int t, n, m;
    static int[] coins;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        t = Integer.parseInt(st.nextToken());
        for (int test_case = 0; test_case < t; test_case++) {
            n = Integer.parseInt(br.readLine());
            coins = new int[n];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                coins[i] = Integer.parseInt(st.nextToken());
            }

            m = Integer.parseInt(br.readLine());
            dp = new int[m + 1];
            dp[0] = 1;
    
            for (int coin : coins) {
                for (int i = coin; i < m + 1; i++) {
                    dp[i] += dp[i - coin];
                }
            }

            sb.append(dp[m]).append("\n");
        }

        System.out.println(sb);

        br.close();
    }
}