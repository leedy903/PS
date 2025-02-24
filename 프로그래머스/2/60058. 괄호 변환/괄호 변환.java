import java.util.*;
import java.io.*;

class Solution {
    public String solution(String p) {
        String answer = "";
        
        answer = getCorrectP(p);
        
        return answer;
    }
    
    public String getCorrectP(String p) {
        if (p.equals("")) {
            return p;
        }
        
        Stack<Character> stack = new Stack<Character>();
        int left = 0;
        int right = 0;
        for (int i = 0; i < p.length(); i++) {
            Character cur = p.charAt(i);
            
            if (cur == ')') {
                left++;
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                }
            }    
            else {
                right++;
                stack.push(cur);
            }
            
            if (left == right) {
                break;
            }
        }
        
        String u = p.substring(0, left + right);
        
        if (stack.isEmpty()) {
            return u + getCorrectP(p.substring(left + right));
        }
        else {
            return '(' + getCorrectP(p.substring(left + right)) + ')' + getCorrectU(u);
        }
    }
    
    public String getCorrectU(String u) {
        String newU = "";
        for (int i = 1; i < u.length() - 1; i++) {
            if (u.charAt(i) == '(') {
                newU += ")";
            }
            else {
                newU += "(";
            }
        }
        return newU;
    }
    
}