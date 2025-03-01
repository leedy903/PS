import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int n;
	static int[] stairs = new int[301];
	static int[] dp = new int[301];
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());

		for(int i = 1; i < n + 1; i++) {
			stairs[i] = Integer.parseInt(br.readLine());
		}
		
		dp[1] = stairs[1];
		dp[2] = stairs[1] + stairs[2];
		
		
		for(int i = 3; i < n + 1; i++) {
			dp[i] = Math.max(dp[i - 3] + stairs[i - 1], dp[i - 2]) + stairs[i];
		}
		
		System.out.println(dp[n]);
		
		br.close();
	}
}