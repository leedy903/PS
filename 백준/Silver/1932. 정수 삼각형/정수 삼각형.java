import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[][] matrix;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        matrix = new int[n][n];
        dp = new int[n][n];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < i + 1; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = matrix[0][0];

        for(int i = 1; i < n; i++) {
            dp[i][0] = dp[i - 1][0] + matrix[i][0];
            for(int j = 1; j < i; j++ ) {
                dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j];
            }
            dp[i][i] = dp[i - 1][i - 1] + matrix[i][i];
        }

        System.out.println(Arrays.stream(dp[n - 1]).max().getAsInt());

        br.close();
    }   
}