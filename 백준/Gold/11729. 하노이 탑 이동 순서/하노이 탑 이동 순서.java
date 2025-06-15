import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static int cnt = 0;
    public static StringBuilder sb;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        hanoi(N, 1, 2, 3);

        System.out.println(cnt);
        System.out.println(sb);
        br.close();
    }

    public static void hanoi(int N, int from, int mid, int to) {
        if (N == 1) {
            cnt++;
            sb.append(from).append(" ").append(to).append("\n");
            return;
        }

        hanoi(N - 1, from, to, mid);
        sb.append(from).append(" ").append(to).append("\n");
        cnt++;
        hanoi(N - 1, mid, from, to);
    }
}
