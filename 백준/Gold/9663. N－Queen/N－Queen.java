import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void dfs(int x) {
        if (x == n) {
            count++;
            return;
        }
        for(int y = 0; y < n; y++) {
            if(isSafe(y, x)) {
                row[x] = y;
                dfs(x + 1);
            }
        }
    }

    public static boolean isSafe(int y, int x) {
        for(int i = 0; i < x; i++) {
            if(y == row[i] || x - i == Math.abs(row[i] - y)) return false;
        }
        return true;
    }

    static int n, count = 0;
    static int[] row;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        row = new int[n];

        dfs(0);
        System.out.println(count);

        br.close();
        bw.close();
        
    }
}
