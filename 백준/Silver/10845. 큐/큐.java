import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class MyQueue {
    int start;
    int end;
    int [] queue;

    public MyQueue(int size){
        this.queue = new int [size];
        this.start = 0;
        this.end = 0;
    }

    public void push(int x) {
        queue[end++] = x;
    }

    public int pop() {
        if(start == end) return -1;
        else return queue[start++];
    }

    public int size() {
        return end - start;
    }

    public int empty() {
        if(start == end) return 1;
        else return 0;
    }

    public int front() {
        if(start == end) return -1;
        else return queue[start];
    }

    public int back() {
        if (start == end) return -1;
        else return queue[end - 1];
    }

}

public class Main {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());

        MyQueue myQueue = new MyQueue(n);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String inputCommand = st.nextToken();
            if(inputCommand.equals("push")) {
                int inputNum = Integer.parseInt(st.nextToken());
                myQueue.push(inputNum);
            }
            else if(inputCommand.equals("pop")) {
                sb.append(myQueue.pop()).append('\n');
            }
            else if(inputCommand.equals("size")) {
                sb.append(myQueue.size()).append('\n');
            }
            else if(inputCommand.equals("empty")) {
                sb.append(myQueue.empty()).append('\n');
            }
            else if(inputCommand.equals("front")) {
                sb.append(myQueue.front()).append('\n');
            }
            else if(inputCommand.equals("back")) {
                sb.append(myQueue.back()).append('\n');
            }
        }

        System.out.println(sb);

        br.close();
    }
}
