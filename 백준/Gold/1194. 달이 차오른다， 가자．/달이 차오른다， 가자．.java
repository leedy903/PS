import java.io.*;
import java.util.*;

class Point {
    int y;
    int x;
    int keyBit;
    Point (int y, int x, int keyBit) {
        this.y = y;
        this.x = x;
        this.keyBit = keyBit;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        int n, m, answer = Integer.MAX_VALUE;
        Point start = null;
        char[][] matrix;
        int[][][] dp;
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, -1, 0, 1};
        
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        matrix = new char[n][m];
        dp = new int[n][m][(int) Math.pow(2, 6)];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);
            }
        }

        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {

                char v = row.charAt(j);
                matrix[i][j] =  v;
                if (v == '0') {
                    start = new Point(i, j, 0);
                    matrix[i][j] = '.';
                }
            }            
        }
        
        Deque<Point> deq = new ArrayDeque<>();
        deq.offer(start);
        dp[start.y][start.x][0] = 0;

        while (!deq.isEmpty()) {
            Point cur = deq.poll();
            int next = dp[cur.y][cur.x][cur.keyBit] == Integer.MAX_VALUE ? Integer.MAX_VALUE : dp[cur.y][cur.x][cur.keyBit] + 1;

            for (int d = 0; d < 4; d++) {
                int ny = cur.y + dy[d];
                int nx = cur.x + dx[d];
                if (0 <= ny && ny < n && 0 <= nx && nx < m) {
                    int keyId;
                    if (matrix[ny][nx] == '#') {
                        continue;
                    }
                    else if (matrix[ny][nx] == '.' && dp[ny][nx][cur.keyBit] > next) {
                        dp[ny][nx][cur.keyBit] = next;
                        deq.offer(new Point(ny, nx, cur.keyBit));
                    }
                    else if (matrix[ny][nx] == '1') {
                        if (dp[ny][nx][cur.keyBit] >= next) {
                            dp[ny][nx][cur.keyBit] = next;
                        }
                        answer = Math.min(answer, dp[ny][nx][cur.keyBit]);
                    }
                    else if ('a' <= matrix[ny][nx] && matrix[ny][nx] <= 'f') {
                        keyId = 1 << (int) matrix[ny][nx] - 'a';
                        if (((cur.keyBit & keyId) != keyId) && dp[ny][nx][cur.keyBit] > next) {
                            int nKeyBit = cur.keyBit | keyId;
                            dp[ny][nx][nKeyBit] = next;
                            deq.offer(new Point(ny, nx, nKeyBit));
                        }
                        else if (dp[ny][nx][cur.keyBit] > next) {
                            dp[ny][nx][cur.keyBit] = next;
                            deq.offer(new Point(ny, nx, cur.keyBit));
                        }
                    }
                    else if ('A' <= matrix[ny][nx] && matrix[ny][nx] <= 'F') {
                        keyId = 1 << (int) matrix[ny][nx] - 'A';
                        if (((cur.keyBit & keyId) == keyId) && dp[ny][nx][cur.keyBit] > next) {
                            dp[ny][nx][cur.keyBit] = next;
                            deq.offer(new Point(ny, nx, cur.keyBit));
                        }
                    }
                }
            }
        }

        answer = answer == Integer.MAX_VALUE ? -1 : answer;
        System.out.println(answer);
        br.close();
    }
}
