import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Horse implements Cloneable {
    int y;
    int x;
    int d;
    boolean isWin;
    public Horse(int y, int x, int d, boolean isWin) {
        this.y = y;
        this.x = x;
        this.d = d;
        this.isWin = isWin;
    }
    @Override
    public Horse clone() throws CloneNotSupportedException {
        return (Horse) super.clone();
    }
    @Override
    public String toString() {
        return String.format("%d %d %d %s\t", y, x, d, isWin);
    }
}

public class Main {
    public static int n, m;
    public static int answer;
    public static int[] scores;
    public static int[][] matrix = {
        { 0,  0,  0,  0,  0,  0,  0,  0,  0},
        { 0,  0,  4,  2, 40, 38, 36,  0,  0},
        { 0,  6,  0,  0, 35,  0,  0, 34,  0},
        { 8,  0,  0,  0, 30,  0,  0,  0, 32},
        {10, 13, 16, 19, 25, 26, 27, 28, 30},
        {12,  0,  0,  0, 24,  0,  0,  0, 28},
        { 0, 14,  0,  0, 22,  0,  0, 26,  0},
        { 0,  0, 16, 18, 20, 22, 24,  0,  0}};
    public static int[] dy = {-1, -1, -1, 0, 1, 1, 1, 0, 0};
    public static int[] dx = {-1, 0, 1, 1, 1, 0, -1, -1, 0};
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        scores = new int[10];
        n = matrix.length;
        m = matrix[0].length;

        for (int i = 0; i < scores.length; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0, 0, new Horse[]{new Horse(0, 3, 5, false), new Horse(0, 3, 5, false), new Horse(0, 3, 5, false), new Horse(0, 3, 5, false)});
        System.out.println(answer);
        br.close();
    }

    public static void dfs(int index, int score, Horse[] horses) throws CloneNotSupportedException {
        if (index == scores.length) {
            answer = Math.max(answer, score);
            return;
        }

        for (int i = 0; i < 4; i++) {
            // 말 선택
            Horse nHorse = horses[i].clone();
            
            // 이미 끝난 말이면 패스
            int preMove = 0;
            if (nHorse.isWin) continue;
            
            // 시작 처리
            if (nHorse.y == 0 && nHorse.x == 3) {
                nHorse.y = 1;
                nHorse.x = 3;
                nHorse.d = 7;
                preMove = 1;
            }
            
            // 교차로에서 시작하면 먼저 이동
            else if (nHorse.y == n / 2 && nHorse.x == 0) {
                nHorse.x += 1;
                nHorse.d = 3;
                preMove = 1;
            }
            else if (nHorse.y == (n - 1) && nHorse.x == m / 2) {
                nHorse.y -= 1;
                nHorse.d = 1;
                preMove = 1;
            }
            else if (nHorse.y == n / 2 && nHorse.x ==  (m - 1)) {
                nHorse.x -= 1;
                nHorse.d = 7;
                preMove = 1;
            }
            else if (nHorse.y == n / 2 && nHorse.x == m / 2) {
                nHorse.y -= 1;
                nHorse.d = 1;
                preMove = 1;
            } 
            
            for (int j = 0; j < scores[index] - preMove; j++) {         
                int nd = nHorse.d;
                int ny = nHorse.y + dy[nd];
                int nx = nHorse.x + dx[nd];
                
                // 끝에 도착한 경우
                if (ny == 0 && nx == m / 2) {
                    nd = 8;
                    nHorse.isWin = true;
                }
                else if (ny == 1 && nx == m / 2) {
                    nd = 1;
                }
                // 중간 교차로
                else if (ny == n / 2 && nx == m / 2) {
                    nd = 1;
                }
                // 맵을 벗어났거나 0에 도착하면 좌회전
                else if (!(0 < ny && ny < n && 0 <= nx && nx < m) || matrix[ny][nx] == 0) {
                    nd = (nHorse.d - 1 + 8) % 8;
                    ny = nHorse.y + dy[nd];
                    nx = nHorse.x + dx[nd];
                }
                nHorse.d = nd;
                nHorse.y = ny;
                nHorse.x = nx;
            }
            
            // 도착지에 다른 말이 있는지 체크
            boolean isNextEmpty = true;
            for (int j = 0; j < 4; j++) {
                if (i != j && (!(nHorse.y == 0 && nHorse.x == m / 2)) && (nHorse.y == horses[j].y && nHorse.x == horses[j].x)) {
                    isNextEmpty = false;
                }
            }
            
            if (!isNextEmpty) continue;

            Horse[] nHorses = new Horse[4];
            for (int j = 0; j < 4; j++) {
                nHorses[j] = (Horse) horses[j].clone();
            }

            nHorses[i] = nHorse.clone();
            dfs(index + 1, score + matrix[nHorse.y][nHorse.x], nHorses);   
        }
    }
}