import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int count = 0;

        int [] sequence = new int [n + 1];
        
        for(int i = 2; i <= n; i++) {
            if(sequence[i] == 0) {
                for(int j = 1; i * j <= n; j++) {
                    if(sequence[i * j] == 0) {
                        sequence[i * j] = ++count;
                        if(count == k){
                            System.out.println(i * j);
                            break;
                        }
                    }
                }
            }
            if(count == k) break;
        }

        br.close();
    }
}
