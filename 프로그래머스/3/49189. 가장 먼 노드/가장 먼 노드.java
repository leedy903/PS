import java.util.*;

class Solution {
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        int[] distance = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[0] = 0;
        distance[1] = 0;
        
        ArrayDeque<Integer> deque = new ArrayDeque<Integer>();
        ArrayList<Integer>[] edgeList = new ArrayList[n + 1];
        
        for(int i = 0; i < n + 1; i++) {
            edgeList[i] = new ArrayList<Integer>();
        }
        
        for(int[] e : edge) {
            edgeList[e[0]].add(e[1]);
            edgeList[e[1]].add(e[0]);
        }
        
        deque.offer(1);
        while(!deque.isEmpty()) {
            int now = deque.poll();
            int size = edgeList[now].size();
            for(int i = 0; i < size; i++) {
                int next = edgeList[now].get(i);
                if(distance[now] + 1 < distance[next]) {
                    distance[next] = distance[now] + 1;
                    deque.offer(next);
                }
            }
        }
        
        int max = Arrays.stream(distance).max().getAsInt();
        for(int i = 1; i < n + 1; i++) {
            if(distance[i] == max) answer++;
        }
        
        return answer;
    }
}

