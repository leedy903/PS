import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> history = new HashSet<String>();
        int[] answer = {0, 0};

        history.add(words[0]);
        
        for(int i = 1; i < words.length; i++) {
            if (!history.add(words[i]) || words[i].charAt(0) != words[i - 1].charAt(words[i - 1].length() - 1)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            }
        }

        return answer;
    }
}