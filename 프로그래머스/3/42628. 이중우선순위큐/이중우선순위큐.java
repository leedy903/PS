import java.util.*;

class Solution {
    
    public int[] solution(String[] operations) {
        
        PriorityQueue<Integer> minQ = new PriorityQueue<Integer>();
        PriorityQueue<Integer> maxQ = new PriorityQueue<Integer>(Collections.reverseOrder());
            
        for(int i = 0; i < operations.length; i++) {
            String[] operation = operations[i].split(" ");
            String operationType = operation[0];
            int number = Integer.parseInt(operation[1]);
            
            
            if(operationType.equals("I")) {
                minQ.offer(number);
                maxQ.offer(number);
            }
            else if(operationType.equals("D")) {
                if(number == 1 && !maxQ.isEmpty()) {
                    int maxNumber = maxQ.poll();
                    minQ.remove(maxNumber);
                }
                else if(number == -1 && !minQ.isEmpty()) {
                    int minNumber = minQ.poll();
                    maxQ.remove(minNumber);
                }
            }
        }
        
        int[] answer = {0, 0};
        if(!maxQ.isEmpty()) {
            answer[0] = maxQ.poll();
            answer[1] = minQ.poll();
        }
        
        
        return answer;
    }
}