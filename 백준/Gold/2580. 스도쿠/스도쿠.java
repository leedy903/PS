import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Location{
    int y, x;
    public Location(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {

    public static void printMatrix() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append(matrix[i][j]).append(' ');
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }

    public static void dfs(int count) {
        if (findSol) return;

        if(count == emptyList.size()) {
            findSol = true;
            printMatrix();
            return;
        }

        Location location = emptyList.get(count);
        for(int i = 1; i < 10; i++) {
            if(isSafe(location, i)) {
                matrix[location.y][location.x] = i;
                dfs(count + 1);
            }
        }
        matrix[location.y][location.x] = 0;
    }

    public static boolean isSafe(Location location, int candiateNum) {
        for(int i = 0; i < 9; i++) {
            if(candiateNum == matrix[location.y][i] && i != location.x) {
                return false;
            }
            if(candiateNum == matrix[i][location.x] && i != location.y) {
                return false;
            }
        }

        int y = (location.y / 3) * 3;
        int x = (location.x / 3) * 3;

        for(int i = y; i < y + 3; i++) {
            for(int j = x; j < x + 3; j++) {
                if(i == location.y && j == location.x) continue;
                if(candiateNum == matrix[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    static boolean findSol = false;
    static int [][] matrix = new int[9][9];
    static ArrayList<Location> emptyList = new ArrayList<Location>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
                if (matrix[i][j] == 0) {
                    emptyList.add(new Location(i, j));
                }
            }
        }

        dfs(0);
        br.close();
    }
}