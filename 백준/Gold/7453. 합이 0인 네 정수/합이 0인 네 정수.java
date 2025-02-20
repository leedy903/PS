import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] A, B, C, D;
    static int[] AB, CD;
    static long ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        A = new int[n];
        B = new int[n];
        C = new int[n];
        D = new int[n];
        AB = new int[n * n];
        CD = new int[n * n];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st.nextToken());
            D[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                AB[i * n + j] = A[i] + B[j];
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                CD[i * n + j] = C[i] + D[j];
            }
        }

        Arrays.sort(AB);
        Arrays.sort(CD);

        int left = 0, right = n * n - 1;

        while(left < n * n && right > -1) {
            if(AB[left] + CD[right] < 0) {
                left++;
            }
            else if(AB[left] + CD[right] > 0) {
                right--;
            }
            else {
                long left_count = 1, right_count = 1;
                while(left + 1 < n * n && (AB[left] == AB[left + 1])) {
                    left_count++;
                    left++;
                }
                while(right - 1 > -1 && (CD[right] == CD[right - 1])) {
                    right_count++;
                    right--;
                }
                ans += left_count * right_count;
                left++;
            }
        }

        System.out.println(ans);
	
        br.close();
    }
}