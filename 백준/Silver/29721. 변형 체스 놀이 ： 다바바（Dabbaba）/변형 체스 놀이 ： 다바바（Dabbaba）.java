import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Set<Long> origin = new HashSet<>();
        Set<Long> movable = new HashSet<>();
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, -1, 0, 1};
        
        int N, K;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            long y = Long.parseLong(st.nextToken()) - 1;
            long x = Long.parseLong(st.nextToken()) - 1;
            origin.add(y * N + x);
        }

        for (long point : origin) {
            long y = point / N;
            long x = point % N;
            for (int d = 0; d < 4; d++) {
                long ny = y + dy[d] * 2;
                long nx = x + dx[d] * 2;
                long nextPoint = ny * N + nx;
                if (0 <= ny && ny < N && 0 <= nx && nx < N && !origin.contains(nextPoint)) {
                    movable.add(nextPoint);
                }
            }
        }

        System.out.println(movable.size());

        br.close();
    }
}