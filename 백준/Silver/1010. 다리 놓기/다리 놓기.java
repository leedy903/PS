import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int n, m;
        final int MAX_NUM = 31;
        int [][] combination = new int[MAX_NUM][MAX_NUM];
        combination[0][0] = combination[1][0] = combination[1][1] = 1;

        for(int i = 2; i < MAX_NUM; i++) {
            for(int j = 0; j < i + 1; j++) {
                if(j == 0 || j == i) {
                    combination[i][j] = 1;
                }
                else {
                    combination[i][j] = combination[i - 1][j - 1] + combination[i - 1][j];
                }
            }
        }
        
        int t = Integer.parseInt(br.readLine());
        for (int test_case = 0; test_case < t; test_case++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            sb.append(combination[m][n]).append('\n');
            
        }

        System.out.println(sb);
        br.close();
    }
}
