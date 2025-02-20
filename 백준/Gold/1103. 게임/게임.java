import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void dfs(int y,int x) {

        if (dp[y][x] > n * m) {
            return;
        }

        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i] * matrix[y][x];
            int nx = x + dx[i] * matrix[y][x];

            if(0 <= ny && ny < n && 0 <= nx && nx < m) {
                if(matrix[ny][nx] != -1 && dp[ny][nx] < dp[y][x] + 1) {
                    dp[ny][nx] = dp[y][x] + 1;
                    dfs(ny, nx);
                }
            }
        }
    }

    static int n, m, maxCount;
    static int [][] matrix, dp;

    static int [] dy = {-1, 0, 1, 0};
    static int [] dx = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        matrix = new int[n][m];
        dp = new int[n][m];

        for(int i = 0; i < n; i++) {
            String matrixInput = br.readLine();
            for(int j = 0; j < m; j++) {
                if(matrixInput.charAt(j) == 'H') {
                    matrix[i][j] = -1;
                }
                else {
                    matrix[i][j] = matrixInput.charAt(j) - 48;
                }
            }
        }

        dp[0][0] = 1;
        dfs(0, 0);

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                maxCount = Math.max(dp[i][j], maxCount);
            }
        }

        if (maxCount > n * m) maxCount = -1;
        System.out.println(maxCount);

        br.close();
        bw.flush();
        bw.close();

    }
}
