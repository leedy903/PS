import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int N, K, sum = 0;
        int[] scores;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        scores = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int score = Integer.parseInt(st.nextToken());
            scores[i] = score;
            sum += score;
        }

        int start = 0, end = sum;
        while (start <= end) {
            int mid = (start + end) / 2;
            int gSum = 0, gCnt = 0;
            for (int i = 0; i < N; i++) {
                gSum += scores[i];
                if (mid <= gSum) {
                    gSum = 0;
                    gCnt++;
                }
            }
            if (gCnt < K) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        System.out.println(end);
        br.close();
    }
}
