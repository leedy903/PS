import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Pair {
    int value, index;

    public Pair(int value, int index){
        this.value = value;
        this.index = index;
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        ArrayDeque<Pair> deque = new ArrayDeque<>();
        
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        int now;

        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++) {
            now = Integer.parseInt(st.nextToken());

            while(!deque.isEmpty() && deque.peek().index <= i - l) {
                deque.pollFirst();
            }

            while(!deque.isEmpty() && deque.peekLast().value >= now) {
                deque.pollLast();
            }
            deque.offer(new Pair(now, i));
            sb.append(deque.peek().value).append(' ');
        }

        System.out.println(sb);
        br.close();
    }
}
