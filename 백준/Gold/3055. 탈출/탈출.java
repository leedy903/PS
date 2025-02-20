import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Location {
    int y, x;
    public Location(int y, int x) {
        this.y = y;
        this.x = x;
    }
}


public class Main {
    static boolean isEscaped = false;
    static final String ESCAPE_FAIL = "KAKTUS";
    static int r, c, time;
    static int [] dy = {-1, 0, 1, 0};
    static int [] dx = {0, -1, 0, 1};

    static char [][] matrix;
    static boolean [][] visit;

    static Queue<Location> hedgehog;
    static Queue<Location> water;

    static Location destination;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        matrix = new char[r][c];
        visit = new boolean[r][c];

        String row;

        hedgehog = new LinkedList<Location>();
        water = new LinkedList<Location>();

        for(int i = 0; i < r; i++) {
            row = br.readLine();
            for(int j = 0; j < c; j++) {
                matrix[i][j] = row.charAt(j);
                if (matrix[i][j] == '*'){
                    water.offer(new Location(i, j));
                }
                if (matrix[i][j] == 'S') {
                    matrix[i][j] = '.';
                    hedgehog.offer(new Location(i, j));
                    visit[i][j] = true;
                }
                if (matrix[i][j] == 'D') {
                    destination = new Location(i, j);
                }
            }
        }

        bfs();
        if(isEscaped) System.out.println(time);
        else System.out.println(ESCAPE_FAIL);

        br.close();
    }

    static void bfs() {
        for (time = 1; ;time++) {
            int waterSize = water.size();
            for(int i = 0; i < waterSize; i++) {
                Location now = water.poll();
                for (int j = 0; j < 4; j++) {
                    int ny = now.y + dy[j];
                    int nx = now.x + dx[j];

                    if(0 <= ny && ny < r && 0 <= nx && nx < c) {
                        if(matrix[ny][nx] == '.') {
                            matrix[ny][nx] = '*';
                            water.offer(new Location(ny, nx));
                        }
                    }
                    
                }
            }

            int hedgehogSize = hedgehog.size();

            if(hedgehogSize == 0) {
                return;
            }

            for(int i = 0; i < hedgehogSize; i++) {
                Location now = hedgehog.poll();
                for (int j = 0; j < 4; j++) {
                    int ny = now.y + dy[j];
                    int nx = now.x + dx[j];

                    if(0 <= ny && ny < r && 0 <= nx && nx < c) {
                        if(matrix[ny][nx] == '.' && !visit[ny][nx]) {
                            visit[ny][nx] = true;
                            hedgehog.offer(new Location(ny, nx));
                        }
                        if(matrix[ny][nx] == 'D') {
                            isEscaped = true;
                            return;
                        }
                    }
                    
                }
            }
        }
    }
}