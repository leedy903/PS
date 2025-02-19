import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		int n, m, answer = 0;
		int[] highers;
		int[] lowers;
		List<Integer>[] upGraph;
		List<Integer>[] downGraph;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		highers = new int[n];
		lowers = new int[n];
		
		upGraph = new ArrayList[n];
		downGraph = new ArrayList[n];
		
		for (int i = 0; i < n; i++) {
			upGraph[i] = new ArrayList<>();
			downGraph[i] = new ArrayList<>();
		}
		
		int u, v;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken()) - 1;
			v = Integer.parseInt(st.nextToken()) - 1;
			upGraph[u].add(v);
			downGraph[v].add(u);
		}
		
		for (int i = 0; i < n; i++) {
			boolean[] visited;
			Deque<Integer> deq;
			
			deq = new ArrayDeque<>();
			visited = new boolean[n];
			
			deq.offer(i);
			visited[i] = true;
			
			while(!deq.isEmpty()) {
				int cur = deq.poll();
				for (int j = 0; j < upGraph[cur].size(); j++) {
					int next= upGraph[cur].get(j);
					if (!visited[next]) {						
						highers[i]++;
						deq.offer(next);
						visited[next] = true;
					}
				}
			}
			
			deq = new ArrayDeque<>();
			visited = new boolean[n];
			
			deq.offer(i);
			visited[i] = true;
			
			while(!deq.isEmpty()) {
				int cur = deq.poll();
				for (int j = 0; j < downGraph[cur].size(); j++) {
					int next= downGraph[cur].get(j);
					if (!visited[next]) {						
						lowers[i]++;
						deq.offer(next);
						visited[next] = true;
					}
				}
			}
			
			
		}
		
		for (int i = 0; i < n; i++) {
			if (highers[i] + lowers[i] == n - 1) {
				answer++;
			}
		}
		
		System.out.println(answer);
		
		br.close();
	}
}
