import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        Set<Integer> sums = new HashSet<Integer>();
        int[] dp = new int[elements.length];
        Arrays.fill(dp, 0);
        
        for (int len = 1; len <= elements.length; len++) {
            for (int i = 0; i < elements.length; i++) {
                dp[i] += elements[(len + i - 1) % elements.length];
                sums.add(dp[i]);
            }
        }
        
        answer = sums.size();
        return answer;
    }
}