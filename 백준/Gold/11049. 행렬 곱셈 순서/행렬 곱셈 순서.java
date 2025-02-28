import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[] r;
	static int[] c;
	static final int INF = Integer.MAX_VALUE;
	static int[][] dp;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		n = Integer.parseInt(br.readLine());
		r = new int[n];
		c = new int[n];
		dp = new int[n][n];
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				dp[i][j] = INF;
			}
		}
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			r[i] = Integer.parseInt(st.nextToken());
			c[i] = Integer.parseInt(st.nextToken());
		}
		
		System.out.println(divideConquer(0, n - 1));
		
		br.close();
	}
	
	
	public static int divideConquer(int start, int end) {
		if(start == end) {
			dp[start][end] = 0;
			return dp[start][end];
		}
		
		if(dp[start][end] != INF) {
			return dp[start][end];
		}
		
		for(int k = start; k < end; k++) {
			int left = divideConquer(start, k);
			int right = divideConquer(k + 1, end);
			dp[start][end] = Math.min(dp[start][end], left + right + r[start] * c[k] * c[end]);
		}
		
		return dp[start][end];
	}
}