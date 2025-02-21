import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        char[] words = word.toCharArray();
        
        String result = "";
        
        for(char w : words) {
            if(Character.isUpperCase(w)) {
                result += Character.toLowerCase(w);
            }
            else{
                result += Character.toUpperCase(w);
            }
        }
        
        System.out.println(result);
        
        sc.close();
    }
}