import java.util.*;
import java.io.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int countP = 0;
        int countY = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char letter = Character.toLowerCase(s.charAt(i));
            if (letter == 'p') {
                countP++;
            }
            if (letter == 'y') {
                countY++;
            }
        }
        
        if (countP != countY) {
            answer = false;
        }

        return answer;
    }
}