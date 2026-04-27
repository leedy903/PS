import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

class Point {
    int y;
    int x;

    public Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    static int n, m;
    static int [][] matrix;
    static int [][] dp;
    static int[] dy = {0, 1, 1};
    static int[] dx = {1, 0, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        matrix = new int[n + 1][m + 1];
        dp = new int[n + 1][m + 1];

        for(int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j < m + 1; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        

        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < m + 1; j++) {
                int maxNum = Math.max(dp[i][j - 1], dp[i - 1][j]);
                dp[i][j] = Math.max(dp[i - 1][j - 1], maxNum) + matrix[i][j];
            }
        }

        System.out.println(dp[n][m]);

        br.close();
        
    }
}