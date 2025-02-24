import java.io.*;
import java.util.*;

class Solution {
    public int[] dy = {-1, 1, 0, 0};
    public int[] dx = {0, 0, -1, 1};
    
    public boolean[][] visited = new boolean[11][11];
    public Map<Character, int[]> direction = new HashMap<Character, int[]>();
    public Set<String> paths = new HashSet<String>();
    
    public int solution(String dirs) {
        int answer = 0;
        
        direction.put('U', new int[] {-1, 0});
        direction.put('D', new int[] {1, 0});
        direction.put('R', new int[] {0, 1});
        direction.put('L', new int[] {0, -1});
        
        int y = 5, x = 5;
        
        for (int i = 0; i < dirs.length(); i++) {
            int[] dir = direction.get(dirs.charAt(i));
            
            int ny = y + dir[0];
            int nx = x + dir[1];
            
            if (0 <= ny && ny < 11 && 0 <= nx && nx < 11) {
                String cur = Integer.toString(y) + Integer.toString(x);
                String next = Integer.toString(ny) + Integer.toString(nx);
                paths.add(cur + next);
                paths.add(next + cur);
                y = ny;
                x = nx;
            }
        }
        answer = paths.size() / 2;
        return answer;
    }
}