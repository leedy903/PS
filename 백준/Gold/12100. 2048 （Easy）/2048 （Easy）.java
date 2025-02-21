import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int max_block_score = 0;
    static int[][] matrix;
    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = {0, -1, 0, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        matrix = new int[n][n];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(matrix, 0);
        
        System.out.println(max_block_score);
        
        br.close();
    }
    
    public static int getMaxScore(int[][] cur_matrix) {
        int block_score = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                block_score = Math.max(block_score, cur_matrix[i][j]);
            }
        }
        return block_score;
    }
    
    
    public static int[][] move(int[][] cur_matrix, int direction) {
        
        boolean[][] is_combined = new boolean[n][n];
        int[][] next_matrix = new int[n][n];

        if(direction < 2) {
            for(int y = 0; y < n; y++) {
                for(int x = 0; x < n; x++) {

                    int ny, nx;
                    int cur_block = cur_matrix[y][x];

                    if(cur_block == 0) continue;

                    for(int i = 1; i < n + 1; i++) {
                        ny = y + dy[direction] * i;
                        nx = x + dx[direction] * i;
                    
                        // 범위 밖
                        if(ny < 0 || ny >= n || nx < 0 || nx >= n) {
                            ny -= dy[direction];
                            nx -= dx[direction];
                            next_matrix[ny][nx] = cur_block;
                            break;
                        }

                        // 앞에 블록이 존재
                        if(next_matrix[ny][nx] != 0) {
                            int next_block = next_matrix[ny][nx];

                            // 같은 값이고 합쳐진 적이 없음
                            if(next_block == cur_block && !is_combined[ny][nx]) {
                                next_matrix[ny][nx] = cur_block << 1;
                                is_combined[ny][nx] = true;
                            }

                            // 다른 값이거나 이미 합쳐짐
                            else {
                                ny -= dy[direction];
                                nx -= dx[direction];
                                next_matrix[ny][nx] = cur_block;
                            }

                            break;
                        }
                    }
                }
            }
        }
        else {
            for(int y = n - 1; y > -1 ; y--) {
                for(int x = n - 1; x > -1; x--) {

                    int ny, nx;
                    int cur_block = cur_matrix[y][x];

                    if(cur_block == 0) continue;

                    for(int i = 1; i < n + 1; i++) {
                        ny = y + dy[direction] * i;
                        nx = x + dx[direction] * i;
                    
                        // 범위 밖
                        if(ny < 0 || ny >= n || nx < 0 || nx >= n) {
                            ny -= dy[direction];
                            nx -= dx[direction];
                            next_matrix[ny][nx] = cur_block;
                            break;
                        }

                        // 앞에 블록이 존재
                        if(next_matrix[ny][nx] != 0) {
                            int next_block = next_matrix[ny][nx];

                            // 같은 값이고 합쳐진 적이 없음
                            if(next_block == cur_block && !is_combined[ny][nx]) {
                                next_matrix[ny][nx] = cur_block << 1;
                                is_combined[ny][nx] = true;
                            }

                            // 다른 값이거나 이미 합쳐짐
                            else {
                                ny -= dy[direction];
                                nx -= dx[direction];
                                next_matrix[ny][nx] = cur_block;
                            }
                            
                            break;
                        }
                    }
                }
            }
        }
        return next_matrix;
    }

    public static void dfs(int[][] cur_matrix, int depth) {
        
        if(depth == 5) {
            int cur_block_score = getMaxScore(cur_matrix);
            max_block_score = Math.max(max_block_score, cur_block_score);
            return;
        }
        
        int[][] copy_map = new int[n][n];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                copy_map[i][j] = cur_matrix[i][j];
            }
        }

        for(int i = 0; i < 4; i++) {
            dfs(move(copy_map, i), depth + 1);
        }
    }
}