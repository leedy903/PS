import java.util.*;
import java.io.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        Stack<Character> stack;
        for (int i = 0; i < s.length(); i++) {
            stack = new Stack<Character>();
            for (int j = 0; j < s.length(); j++) {
                Character now = s.charAt((i + j) % s.length());
                if (now == ')' && !stack.empty() && stack.peek() == '(') {
                    stack.pop();
                }
                else if (now == ']' && !stack.empty() && stack.peek() == '[') {
                    stack.pop();
                }
                else if (now == '}' && !stack.empty() && stack.peek() == '{') {
                    stack.pop();
                }
                else {
                    stack.push(now);
                }
            }
            if (stack.empty()) {
                answer += 1;
            }
        }
        
        return answer;
    }
}