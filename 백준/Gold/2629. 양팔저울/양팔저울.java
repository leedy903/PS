import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] weights;
    static int[] marbles;
    static boolean[][] dp;
    static final String isPossible = "Y ";
    static final String isImpossible = "N ";
    static final int maxWeight = 40_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        weights = new int[n + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++) {
            weights[i] = Integer.parseInt(st.nextToken());
        }

        m = Integer.parseInt(br.readLine());
        marbles = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            marbles[i] = Integer.parseInt(st.nextToken());
        }

        dp = new boolean[n + 1][maxWeight + 1];

        for (int i = 1; i < n + 1; i++) {
            int weight = weights[i];
            dp[i][weight] = true;
            for (int j = 1; j <= maxWeight; j++) {
                if (dp[i - 1][j] == true) {
                    dp[i][j] = dp[i - 1][j];
                    dp[i][Math.abs(j - weight)] = true;
                    dp[i][j + weight] = true;
                }
            }
        }

        for (int marble : marbles) {
            if (dp[n][marble] == true) {
                sb.append(isPossible);
            }
            else {
                sb.append(isImpossible);
            }
        }

        System.out.println(sb);
        br.close();
    }
}
