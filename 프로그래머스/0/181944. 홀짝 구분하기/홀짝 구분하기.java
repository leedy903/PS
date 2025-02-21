import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        
        sb.append(n).append(" is ");
        
        if((n & 1) == 1) sb.append("odd");
        else sb.append("even");
        
        System.out.println(sb);
        
        br.close();
    }
}