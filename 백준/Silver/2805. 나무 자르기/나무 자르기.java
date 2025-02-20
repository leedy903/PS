import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[] trees;
    static int maxHeight = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        trees = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
        }


        int start = 0;
        int end = Arrays.stream(trees).max().getAsInt();
        while (start <= end) {
            int mid = (start + end) / 2;
            long sumCutTree = 0;
            for (int i = 0; i < n; i++) {
                sumCutTree += Math.max(trees[i] - mid, 0);
            }
            if (sumCutTree >= m) {
                maxHeight = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        
        System.out.println(maxHeight);
        
        br.close();
    }
}