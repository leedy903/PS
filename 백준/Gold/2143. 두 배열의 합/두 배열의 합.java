import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int t, n, m;
    static long ans = 0;
    static int[] arr_a, arr_b;
    static int[] sum_a, sum_b;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        t = Integer.parseInt(br.readLine());
        n = Integer.parseInt(br.readLine());
        arr_a = new int[n];
        sum_a = new int[n * (n + 1) / 2];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            arr_a[i] = Integer.parseInt(st.nextToken());
        }

        int step = 0;
        for(int i = 0; i < n; i++) {
            sum_a[step] = arr_a[i];
            for(int j = 1; j < n - i; j++) {
                sum_a[step + j] = sum_a[step + j - 1] + arr_a[j + i];
            }
            step += n - i;
        }

        m = Integer.parseInt(br.readLine());
        arr_b = new int[m];
        sum_b = new int[m * (m + 1) / 2];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++) {
            arr_b[i] = Integer.parseInt(st.nextToken());
        }

        step = 0;
        for(int i = 0; i < m; i++) {
            sum_b[step] = arr_b[i];
            for(int j = 1; j < m - i; j++) {
                sum_b[step + j] = sum_b[step + j - 1] + arr_b[j + i];
            }
            step += m - i;
        }
        
        Arrays.sort(sum_a);
        Arrays.sort(sum_b);

        int left = 0, right = sum_b.length - 1;
        long sum = 0;
        while(left < sum_a.length && right > -1) {
            long sum_left = sum_a[left], sum_right = sum_b[right];
            sum = sum_left + sum_right;
            if(sum == t) {
                long left_ans = 0, right_ans = 0;
                while(left < sum_a.length && sum_a[left] == sum_left ) {
                    left++;
                    left_ans++;
                }
                while(right > -1 && sum_b[right] == sum_right) {
                    right--;
                    right_ans++;
                }
                ans += left_ans * right_ans;
            }
            else if(sum > t) {
                right--;
            }
            else if(sum < t) {
                left++;
            }
        }

        System.out.println(ans);

        br.close();

    }
}