import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] dp = new int[10];
        Arrays.fill(dp, 1);
        for(int i = 1; i < n; i++) {
            for(int j = 1; j < 10; j++) {
                dp[j] += dp[j - 1]%10007;
            }
        }
        System.out.println(Arrays.stream(dp).sum()%10007);
        sc.close();
    }
}