import java.io.*;
class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;     
        long min = r1;
        long max = r2;
        for (long i = 0; i < max; i++) {
            long count = (long) (Math.floor(Math.sqrt(max * max - i * i)) - Math.ceil(Math.sqrt(Math.max(0, min * min - i * i))));
            answer += i >= min ? count : count + 1;
        }
        
        return answer * 4;
    }
}