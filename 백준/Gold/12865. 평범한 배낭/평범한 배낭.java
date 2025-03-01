import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, k;
    static int[] weight;
    static int[] value;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        weight = new int[n + 1];
        value = new int[n + 1];

        dp = new int[n + 1][k + 1];

        for(int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            weight[i] = Integer.parseInt(st.nextToken());
            value[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 1; i < n + 1; i++) {
            for(int capable = 1; capable < k + 1; capable++) {
                if(capable - weight[i] >= 0) {
                    dp[i][capable] = Math.max(dp[i - 1][capable - weight[i]] + value[i], dp[i - 1][capable]);
                }
                else {
                    dp[i][capable] = dp[i - 1][capable];
                }
            }
        }

        System.out.println(dp[n][k]);

        br.close();
    }
}