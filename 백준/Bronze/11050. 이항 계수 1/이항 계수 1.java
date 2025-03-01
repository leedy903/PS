import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        System.out.println(factorial(n) / (factorial(k) * factorial(n - k)));

        br.close();
    }

    static int factorial(int number) {
        int ret;
        for(ret = 1; number > 0; number --) {
            ret *= number;
        }
        return ret;
    }
}
