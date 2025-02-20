import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int count = 0;

    static int[] numbers;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        numbers = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = 0;
        int sum = 0;

        while (start < n) {
            if (sum == m) {
                count++;
            }
            if (sum > m || end == n) {
                sum -= numbers[start];
                start++;
            }
            else {
                sum += numbers[end];
                end++;
            }
        }

        System.out.println(count);

    }
}