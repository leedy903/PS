import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Stack<Integer> subBelt = new Stack<Integer>();
        
        for (int i = 0;  i < order.length; i++) {
            subBelt.push(i + 1);
            while (!subBelt.isEmpty()) {
                if (subBelt.peek() == order[answer]) {
                    subBelt.pop();
                    answer++;
                } else break;
            }
        }
        
        return answer;
    }
}