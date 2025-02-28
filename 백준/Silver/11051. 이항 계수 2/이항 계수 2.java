import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int MOD_NUM = 10_007;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int [][] combination = new int[n + 1][n + 1];
        combination[0][0] = combination[1][0] = combination[1][1] = 1;

        for(int i = 2; i < n + 1; i++) {
            for(int j = 0; j < i + 1; j++) {
                if(j == 0 || j == i) {
                    combination[i][j] = 1;
                }
                else {
                    combination[i][j] = (combination[i - 1][j - 1] + combination[i - 1][j]) % MOD_NUM;
                }
            }
        }

        System.out.println(combination[n][k]);

        br.close();
    }

    static int factorial(int number) {
        int ret;
        for(ret = 1; number > 0; number --) {
            ret = (ret * number) % MOD_NUM;
        }
        return ret;
    }
}