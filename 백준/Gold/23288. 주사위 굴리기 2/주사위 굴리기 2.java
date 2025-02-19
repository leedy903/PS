import java.io.*;
import java.util.*;

class Dice {
    Point point;
    int direction;
    int [][] devMap = {{0, 2, 0}, {4, 1, 3}, {0, 5, 0}, {0, 6, 0}};
    Dice() {
        point = new Point(0, 0);
        direction = 3;
    }
}

class Point {
    int y;
    int x;
    Point (int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    public static int n, m, k;
    public static int [][] matrix;
    public static int [] dy = {-1, 0, 1, 0};
    public static int [] dx = {0, -1, 0, 1};
    public static Dice dice;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        
        dice = new Dice();

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        matrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }    
        }

        int answer = 0;
        for (int i = 0; i < k; i++) {
            roll();
            answer += getScore();
        }

        System.out.println(answer);

        br.close();
    }

    public static void roll() {       
        Point cur = dice.point;
        int ny = cur.y + dy[dice.direction];
        int nx = cur.x + dx[dice.direction];
        if (!(0 <= ny && ny < n && 0 <= nx && nx < m)) {
            dice.direction = (dice.direction + 2) % 4;
        }
        
        ny = cur.y + dy[dice.direction];
        nx = cur.x + dx[dice.direction];

        dice.point.y = ny;
        dice.point.x = nx;

        Deque<Integer> deq = new ArrayDeque<>();
        // 남북
        if (dice.direction % 2 == 0) {
            for (int i = 0; i < 4; i++) {
                deq.offer(dice.devMap[i][1]);
            }
        }

        // 동서
        if (dice.direction % 2 == 1) {
            for (int i = 0; i < 3; i++) {
                deq.offer(dice.devMap[1][i]);
            }
            deq.offer(dice.devMap[3][1]);
        }

        // 회전
        if (dice.direction < 2){
            deq.offer(deq.poll());
        } else {
            deq.offerFirst(deq.pollLast());
        }
            
        // 남북
        if (dice.direction % 2 == 0) {
            for (int i = 0; i < 4; i++) {
                dice.devMap[i][1] = deq.poll();
            }
        }

        // 동서
        if (dice.direction % 2 == 1) {
            for (int i = 0; i < 3; i++) {
                dice.devMap[1][i] = deq.poll();
            }
            dice.devMap[3][1] = deq.poll();
        }

        if (dice.devMap[3][1] < matrix[dice.point.y][dice.point.x]) {
            dice.direction = (dice.direction + 1) % 4;
        } else if (dice.devMap[3][1] > matrix[dice.point.y][dice.point.x]) {
            dice.direction = (dice.direction + 3) % 4;
        }
        
    }

    public static int getScore() {
        Point point = dice.point;
        int score = matrix[point.y][point.x];
        int count = 1;
        boolean[][] visited = new boolean[n][m];
        Deque<Point> deq = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            Arrays.fill(visited[i], false);
        }

        deq.offer(point);
        visited[point.y][point.x] = true;
        while (!deq.isEmpty()) {
            Point cur = deq.poll();
            for (int i = 0; i < 4; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];
                if (0 <= ny && ny < n && 0 <= nx && nx < m) {
                    if (matrix[ny][nx] == score && !visited[ny][nx]) {
                        count++;
                        visited[ny][nx] = true;
                        deq.offer(new Point(ny, nx));
                    }
                }
            }
        }

        return score * count;
    }

}
