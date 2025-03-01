import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        boolean[] prime_number;
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        StringBuilder sb = new StringBuilder();

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        prime_number = new boolean[n + 1];
        Arrays.fill(prime_number, true);

        prime_number[0] = false;
        prime_number[1] = false;

        for(int i = 2; i < n + 1; i++) {
            if(prime_number[i]) {
                if(i >= m) {
                    sb.append(i).append('\n');
                }
                for(int j = 2; i * j < n + 1; j++) {
                    prime_number[i * j] = false;
                }
            }
        }
        System.out.print(sb);
    }
}