import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] dp = new int[n][10];

        for(int i = 1; i < 10; i++) {
            dp[0][i] = 1;
        }

        for(int i = 1; i < n; i++) {
            for(int j = 0; j < 10; j++) {
                if(j == 0) {
                    dp[i][j] = dp[i - 1][j + 1];
                }
                else if(j == 9) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                else {
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
                }
            }
        }
        System.out.println(Arrays.stream(dp[n - 1]).mapToLong(i -> i).sum() % 1000000000);
        sc.close();
    }
}