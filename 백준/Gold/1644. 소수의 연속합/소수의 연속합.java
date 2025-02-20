import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int n, ans = 0;
    static Boolean[] isPrime;
    static int[] primeNumber;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        isPrime = new Boolean[n + 1];
        Arrays.fill(isPrime, true);

        isPrime[0] = false;
        isPrime[1] = false;

        int primeCount = 0;
        for(int i = 2; i < n + 1; i++) {
            if(isPrime[i]) {
                primeCount++;
                for(int j = 2; i * j < n + 1; j++) {
                    isPrime[i * j] = false;
                }
            }
        }

        primeNumber = new int[primeCount];

        int index = 0;
        for(int i = 2; i < n + 1; i++) {
            if(isPrime[i]) {
                primeNumber[index++] = i;
            }
        }

        int start = 0, end = 0;
        long sum = 0;
        while(start < primeNumber.length && end <= primeNumber.length) {
            if(sum < n && end < primeNumber.length) {
                sum += primeNumber[end];
                end ++;
            }
            else if(sum > n) {
                sum -= primeNumber[start];
                start++;
            }
            else {
                if(sum == n) ans++;
                sum -= primeNumber[start];
                start++;
            }
        }

        System.out.println(ans);

        br.close();
    }
}