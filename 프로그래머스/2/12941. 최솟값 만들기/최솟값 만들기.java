import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        for(int i = 0; i < B.length; i++) {
            B[i] = -B[i];
        }

        Arrays.sort(B);
        
        for(int i = 0; i < A.length; i++) {
            answer += - A[i] * B[i];
        }

        return answer;
    }
}