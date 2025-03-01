import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class MyStack {
    int top;
    int [] stack;

    public MyStack(int size){
        this.stack = new int [size];
        this.top = -1;
    }

    public void push(int x) {
        stack[++top] = x;
    }

    public int pop() {
        if(top == -1) return -1;
        return stack[top--];
    }

    public int size() {
        return top + 1;
    }

    public int empty() {
        if(top == -1) {
            return 1;
        }
        else return 0;
    }

    public int top() {
        if(top == -1) return -1;
        else return stack[top];
    }

}

public class Main {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());

        MyStack myStack = new MyStack(n);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String inputCommand = st.nextToken();
            if(inputCommand.equals("push")) {
                int inputNum = Integer.parseInt(st.nextToken());
                myStack.push(inputNum);
            }
            else if(inputCommand.equals("pop")) {
                sb.append(myStack.pop()).append('\n');
            }
            else if(inputCommand.equals("size")) {
                sb.append(myStack.size()).append('\n');
            }
            else if(inputCommand.equals("empty")) {
                sb.append(myStack.empty()).append('\n');
            }
            else if(inputCommand.equals("top")) {
                sb.append(myStack.top()).append('\n');
            }
        }

        System.out.println(sb);

        br.close();
    }
}
