import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int n, m;
	static int max_square_length = 0;
	static int[][] matrix;
	static int[][] dp;
	static int[][] range;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		matrix = new int[n + 1][m + 1];
		dp = new int[n + 1][m + 1];
		
		for(int i = 1; i < n + 1; i++) {
			String[] row = br.readLine().split("");
			for(int j = 1; j < m + 1; j++) {
				matrix[i][j] = Integer.parseInt(row[j - 1]);
			}
		}
		
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < m + 1; j++) {
				if(matrix[i][j] == 1) {
					dp[i][j] = 1;
				}
			}
		}
		
		int min_length;
		
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < m + 1; j++) {
				min_length = 0;
				if(dp[i][j] > 0) {					
					
					if(dp[i - 1][j - 1] == 0 || dp[i - 1][j] == 0 || dp[i][j - 1] == 0) {
						continue;
					}
					
					min_length = Math.min(dp[i - 1][j - 1], dp[i - 1][j]);
					min_length = Math.min(min_length, dp[i][j - 1]);
					
					dp[i][j] = min_length + 1;

				}
			}
		}
		
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < m + 1; j++) {
				max_square_length = Math.max(max_square_length, dp[i][j]);
			}
		}
		
		System.out.println(max_square_length * max_square_length);
	}
}

