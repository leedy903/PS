import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int max_len = 10002;
        int t = Integer.parseInt(br.readLine());
        int[] dp = new int[max_len];
        Arrays.fill(dp, 1);
        for (int i = 2; i < 4; i++) {
            for (int j = 0; j < max_len; j++) {
                if (j > i) {
                    dp[j] += dp[j - i];
                }
            }
        }

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            sb.append(dp[n + 1]).append("\n");
        }
        System.out.println(sb);

        br.close();
    }
}