import java.io.*;
import java.util.*;

public class Main {

    static final int MAX_COST = 10001;
    static int minCost = MAX_COST;
    static int n, m;
    static int[] memories;
    static int[] costs;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        StringTokenizer memorySt = new StringTokenizer(br.readLine());
        StringTokenizer costSt = new StringTokenizer(br.readLine());

        memories = new int[n + 1];
        costs = new int[n + 1];
        dp = new int[n + 1][MAX_COST];

        for (int i = 1; i < n + 1; i++) {
            memories[i] = Integer.parseInt(memorySt.nextToken());
            costs[i] = Integer.parseInt(costSt.nextToken());
        }

        for (int i = 1; i < n + 1; i++) {
            int memory = memories[i];
            int cost = costs[i];
            for (int j = 0; j < MAX_COST; j++) {
                if (j >= cost) {
                    dp[i][j] = Math.max(dp[i - 1][j - cost] + memory, dp[i - 1][j]);
                }
                else {
                    dp[i][j] = dp[i - 1][j];
                }
                if (dp[i][j] >= m) {
                    minCost = Math.min(minCost, j);
                }
            }
        }

        System.out.println(minCost);

        br.close();
    }
}