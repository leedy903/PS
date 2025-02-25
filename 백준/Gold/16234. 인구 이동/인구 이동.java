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
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int N, L, R, answer = 0;
        int[][] matrix;
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, -1, 0, 1};

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        matrix = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int day = 0; day <= 2000; day++) {
            boolean isMoved = false;
            boolean[][] visited = new boolean[N][N];
            for (int y = 0; y < N; y++) {
                for (int x = 0; x < N; x++) {
                    if (!visited[y][x]) {
                        int population = matrix[y][x];
                        List<Point> union = new ArrayList<>();
                        union.add(new Point(y, x));
                        Deque<Point> deq = new ArrayDeque<>();
                        deq.offer(new Point(y, x));
                        visited[y][x] = true;
                        while(!deq.isEmpty()) {
                            Point cur = deq.poll();
                            for (int d = 0; d < 4; d++) {
                                int ny = cur.y + dy[d];
                                int nx = cur.x + dx[d];
                                if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                                    int diff = Math.abs(matrix[ny][nx] - matrix[cur.y][cur.x]);
                                    if (!visited[ny][nx] && L <= diff && diff <= R) {
                                        population += matrix[ny][nx];
                                        union.add(new Point(ny, nx));
                                        deq.offer(new Point(ny, nx));
                                        visited[ny][nx] = true;
                                    }
                                }
                            }
                        }
                        population /= union.size();
                        for (Point cur : union) {
                            matrix[cur.y][cur.x] = population;
                        }
                        if (union.size() > 1) {
                            isMoved = true;
                        }
                    }
                }
            }
            if (!isMoved) {
                answer = day;
                break;
            }
        }

        System.out.print(answer);
        br.close();
    }
}