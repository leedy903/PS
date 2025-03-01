import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node {
    int l_child;
    int r_child;
    public Node(int l_child, int r_child) {
        this.l_child = l_child;
        this.r_child = r_child;
    }
}

public class Main {
    static Node [] nodes;
    static int a_ascii = (int) 'A';
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        nodes = new Node[n];
        int root, l_child, r_child;
        

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            root = (int) st.nextToken().charAt(0) - a_ascii;
            l_child = (int) st.nextToken().charAt(0) - a_ascii;
            r_child = (int) st.nextToken().charAt(0) - a_ascii;

            nodes[root] = new Node(l_child, r_child);
        }

        preOrder(0);
        System.out.println();
        inOrder(0);
        System.out.println();
        postOrder(0);
        System.out.println();
        
        br.close();
    }

    public static void preOrder(int index) {
        if (index < 0) return;
        int l_child = nodes[index].l_child;
        int r_child = nodes[index].r_child;

        System.out.print(Character.toString((char) index + a_ascii));
        preOrder(l_child);
        preOrder(r_child);
    }

    public static void inOrder(int index) {
        if (index < 0) return;
        int l_child = nodes[index].l_child;
        int r_child = nodes[index].r_child;

        inOrder(l_child);
        System.out.print(Character.toString((char) index + a_ascii));
        inOrder(r_child);
    }

    public static void postOrder(int index) {
        if (index < 0) return;
        int l_child = nodes[index].l_child;
        int r_child = nodes[index].r_child;

        postOrder(l_child);
        postOrder(r_child);
        System.out.print(Character.toString((char) index + a_ascii));
    }
}
