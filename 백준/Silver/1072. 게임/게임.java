import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        long z = ((long)y * 100) / x;

        int win_count = -1;

        int start = 1;
        int end = 1_000_000_000;
        while(start <= end) {
            int mid = (start + end) / 2;
            long new_win = (((long)y + (long)mid) * 100)/(x + mid);
            
            if (new_win != z){
                win_count = mid;
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }

        System.out.println(win_count);

        br.close();
    }
}
