import java.util.*;

class Solution {
    public String solution(String s) {
        StringTokenizer st = new StringTokenizer(s);
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        int now;
        while(st.hasMoreTokens()) {
            now = Integer.parseInt(st.nextToken());
            min = Math.min(now, min);
            max = Math.max(now, max);
        }
         
        String answer = min + " " + max;
        
        return answer;
    }
}