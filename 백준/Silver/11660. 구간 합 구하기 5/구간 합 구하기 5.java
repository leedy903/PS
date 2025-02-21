import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[][] matrix;
	static int[][] dp;
	static int[][] range;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		matrix = new int[n + 1][n + 1];
		dp = new int[n + 1][n + 1];
		range = new int[m][4];
		
		for(int i = 1; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 1; j < n + 1; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			range[i][0] = Integer.parseInt(st.nextToken());
			range[i][1] = Integer.parseInt(st.nextToken());
			range[i][2] = Integer.parseInt(st.nextToken());
			range[i][3] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = 1; i < n + 1; i++) {
			for(int j = 1; j < n + 1; j++) {
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j];
			}
		}
		
		int start_x, start_y, end_x, end_y, area;
		for(int i = 0; i < m; i++) {
			start_y = range[i][0] - 1;
			start_x = range[i][1] - 1;
			end_y = range[i][2];
			end_x = range[i][3];
			area = dp[end_y][end_x] - dp[end_y][start_x] - dp[start_y][end_x] + dp[start_y][start_x];
			sb.append(area).append("\n");
		}
		
		System.out.print(sb);
		
		br.close();
	}
}
