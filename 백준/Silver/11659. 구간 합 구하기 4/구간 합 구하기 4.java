import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] sequence;
    static int[] sum;
    static int[][] range;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        sequence = new int[n + 1];
        sum = new int[n + 1];
        range = new int[m][2];

        st = new StringTokenizer(br.readLine());
        for(int i = 1; i < n + 1; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            range[i][0] = Integer.parseInt(st.nextToken());
            range[i][1] = Integer.parseInt(st.nextToken());
        }

        for(int i = 1; i < n + 1; i++) {
            sum[i] = sum[i - 1] + sequence[i];
        }


        int start, end;
        for(int i = 0; i < m; i++) {
            start = range[i][0] - 1;
            end = range[i][1];
            sb.append(sum[end] - sum[start]).append("\n");
        }

        System.out.print(sb);

        br.close();
    }
}