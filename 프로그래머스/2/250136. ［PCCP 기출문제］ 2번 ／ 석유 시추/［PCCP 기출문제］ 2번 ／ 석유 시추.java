import java.io.*;
import java.util.*;

class Point {
    int y;
    int x;
    
    Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

class Solution {
    
    public List<Integer> oilPools = new ArrayList<Integer>();
    
    public int solution(int[][] land) {
        int answer = 0;
        int n = land.length;
        int m = land[0].length;
        
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, -1, 0, 1};
        
        oilPools.add(0);
            
        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(visited[i], 0);
        }

        int oilPoolSize = 0;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                int oil = 0;
                if (land[y][x] == 1 && visited[y][x] == 0) {
                    oilPoolSize++;
                    Deque<Point> deq = new ArrayDeque<Point>();
                    deq.offer(new Point(y, x));
                    visited[y][x] = oilPoolSize;
                    oil++;
                    while(!deq.isEmpty()) {
                        Point cur = deq.poll();
                        for (int d = 0; d < 4; d++) {
                            int ny = cur.y + dy[d];
                            int nx = cur.x + dx[d];
                            if (0 <= ny && ny < n && 0 <= nx && nx < m) {
                                if (land[ny][nx] == 1 && visited[ny][nx] == 0) {
                                    deq.offer(new Point(ny, nx));
                                    visited[ny][nx] = oilPoolSize;
                                    oil++;
                                }
                            }
                        }
                    }
                    oilPools.add(oil);
                }
            }
        }
        
        for (int x = 0; x < m; x++) {
            int oil = 0;
            Set<Integer> oilPoolIdxs = new HashSet<Integer>();
            for (int y = 0; y < n; y++) {    
                oilPoolIdxs.add(visited[y][x]);
            }
            for (int oilPoolIdx : oilPoolIdxs) {
                oil += oilPools.get(oilPoolIdx);
            }
            answer = Math.max(answer, oil);
        }
        
        return answer;
    }
}