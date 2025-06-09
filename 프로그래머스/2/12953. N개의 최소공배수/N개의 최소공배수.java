class Solution {
    public int solution(int[] arr) {
        int lcm = 1;
        for (int i = 0; i < arr.length; i++) {
            lcm = 1 * getLcm(lcm, arr[i]);
        }
        return lcm;
    }
    
    public int getGcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    public int getLcm(int a, int b) {
        return a * b / getGcd(a, b);
    }
}