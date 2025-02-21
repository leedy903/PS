import java.util.*;


class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        
        for(int i = 0; i < name.length; i++) {
            map.put(name[i], yearning[i]);
        }
        
        int[] answer = new int[photo.length];
        
        for(int i = 0; i < photo.length; i++) {
            int score = 0;
            for(int j = 0; j < photo[i].length; j++) {
                if(map.containsKey(photo[i][j])) {
                    score += map.get(photo[i][j]);
                }
            }
            answer[i] = score;
        }
        
        
        return answer;
    }
}