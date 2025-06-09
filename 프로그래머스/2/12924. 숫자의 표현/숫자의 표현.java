class Solution {
    
    public int solution(int n) {
        int answer = 0;
        
        int start = 1, end = 1;
        int sum = 0;
        while(start < n + 1 && end < n + 1) {
            if(sum < n && end < n + 1) {
                sum += end;
                end++;
            }
            else if(sum > n) {
                sum -= start;
                start++;
            }
            else{
                answer++;
                sum -= start;
                start++;
            }
        }
            
            
        return answer + 1;
        
    }
     
}