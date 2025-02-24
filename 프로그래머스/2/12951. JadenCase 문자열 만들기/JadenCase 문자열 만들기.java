import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] lowerString = s.toLowerCase().split("");
        
        Boolean isFirst = true;
        
        for(String token : lowerString) {
            if(isFirst) {
                answer += token.toUpperCase();
            }
            else {
                answer += token;    
            }
            
            if(token.equals(" ")) {
                isFirst = true;
            }
            else {
                isFirst = false;
            }
            
        }
        
        return answer;
    }
}