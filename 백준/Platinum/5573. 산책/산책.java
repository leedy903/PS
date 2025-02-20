import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int h, w, n;
    static int [][] matrix;
    static int [][][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        matrix = new int[h + 1][w + 1];
        dp = new int[h + 1][w + 1][2];

        for(int i = 1; i < h + 1; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j < w + 1; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < h + 1; i++) {
            for(int j = 0; j < w + 1; j++) {
                dp[i][j][0] = 0;
                dp[i][j][1] = 0;
            }
        }
        n -= 1;
        dp[0][1][0] = n / 2;
        dp[1][0][1] = n / 2;

        if((n & 1) == 1) {
            if(matrix[1][1] == 1) {
                dp[0][1][0] += 1;
            }
            else if(matrix[1][1] == 0) {
                dp[1][0][1] += 1;
            }
        }

        for(int i = 1; i < h + 1; i++) {
            for(int j = 1; j < w + 1; j++) {
                int count = dp[i - 1][j][0] + dp[i][j - 1][1];

                dp[i][j][0] = count / 2;
                dp[i][j][1] = count / 2;

                if((count & 1) == 1) {
                    dp[i][j][matrix[i][j]] += 1;
                    matrix[i][j] = matrix[i][j] == 0 ? 1: 0;
                }
            }
        }

        int y = 1, x = 1;
        while(y != h + 1 && x != w + 1) {
            if(matrix[y][x] == 0) {
                y += 1;
            }
            else if(matrix[y][x] == 1) {
                x += 1;
            }
        }

        System.out.println(y + " " + x);

        br.close();
    }
}