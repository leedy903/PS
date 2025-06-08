import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int m, n;
    public static int[][] matrix;
    public static int[][] dp;
    public static boolean[][] visited;

    public static int[] dy = {-1, 0, 1, 0};
    public static int[] dx = {0, -1, 0, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        matrix = new int[m][n];
        dp = new int[m][n];
        visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(dfs(0, 0));

        br.close();
    }

    public static int dfs(int y, int x) {
        if (y == m - 1 && x == n - 1) {
            return 1;
        }

        if (!visited[y][x]) {
            visited[y][x] = true;
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (0 <= ny && ny < m && 0 <= nx && nx < n) {
                    if (matrix[y][x] > matrix[ny][nx]) {
                        dp[y][x] += dfs(ny, nx);
                    }
                }
            }
        }

        return dp[y][x];
    }
}