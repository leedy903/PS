import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        Arrays.sort(routes, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[1] - o2[1];
            }
            
        });
        
        int camera = -30001;
        for(int[] route : routes) {
            if(camera < route[0]) {
                answer++;
                camera = route[1];
            }
        }
        
        return answer;
    }
}