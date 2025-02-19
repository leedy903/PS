import java.io.*;
import java.util.*;

class Point {
    int y;
    int x;
    public Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    public static Deque<Point> deq = new ArrayDeque<Point>();
    public static int[] dy = {-1, 0, 1, 0};
    public static int[] dx = {0, -1, 0, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] matrix = new int[n][n];
        int[][] dist = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            String walls = br.readLine();
            for (int j = 0; j < n; j++) {
                matrix[i][j] = walls.charAt(j) - '0';
            }    
        }

        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        deq.offer(new Point(0, 0));
        dist[0][0] = 0;
        while (!deq.isEmpty()) {
            Point now = deq.poll();

            for (int i = 0; i < 4; i++) {
                int ny = now.y + dy[i];
                int nx = now.x + dx[i];

                if (0 <= ny && ny < n && 0 <= nx && nx < n) {
                    if (matrix[ny][nx] == 0 && dist[ny][nx] > dist[now.y][now.x] + 1) {
                        dist[ny][nx] = dist[now.y][now.x] + 1;
                        deq.offerFirst(new Point(ny, nx));
                    }
                    else if (matrix[ny][nx] == 1 && dist[ny][nx] > dist[now.y][now.x]) {
                        dist[ny][nx] = dist[now.y][now.x];
                        deq.offerLast(new Point(ny, nx));
                    }
                }
            }
        }

        System.out.println(dist[n - 1][n - 1]);

        br.close();
    }
}