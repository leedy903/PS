import java.util.*;
import java.io.*;

class Solution {
    static Map<String, Integer> window = new HashMap<String, Integer>();
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        for (int i = 0; i < 9; i++) {
            if (!window.containsKey(discount[i])) {
                window.put(discount[i], 0);
            }
            window.put(discount[i], window.get(discount[i]) + 1);
        }
        
        for (int i = 0; i < discount.length - 9; i++) {
            if (!window.containsKey(discount[i + 9])) {
                window.put(discount[i + 9], 0);
            }
            
            window.put(discount[i + 9], window.get(discount[i + 9]) + 1);
            
            if (check(want, number)) {
                answer++;
            }
            
            window.put(discount[i], window.get(discount[i]) - 1);
            
            if (window.get(discount[i]) == 0) {
                window.remove(discount[i]);
            }
        }
        
        return answer;
    }
    
    public boolean check(String[] want, int[] number) {
        for (int i = 0; i < want.length; i++) {
            if (!window.containsKey(want[i]) || window.get(want[i]) < number[i]) {
                return false;
            }
        }
        return true;
    }
}