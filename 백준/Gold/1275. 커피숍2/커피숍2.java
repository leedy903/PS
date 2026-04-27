import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class IndexedTree {

    int offset;
    long [] tree;

    public IndexedTree(int size) {
        for(offset = 1; offset < size; offset *= 2);
        tree = new long[offset * 2 + 1];
    }

    public void setTree(int[] leaves) {
        for(int i = 0; i < leaves.length; i++) {
            tree[offset + i] = leaves[i];
        }

        for(int i = offset - 1; i > 0; i--) {
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }
    }

    public void update(int index, int value) {
        tree[offset + index - 1] = value;

        for(int i = (offset + index - 1) / 2; i > 0; i /= 2) {
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }
    }

    public long getSum(int left, int right) {
        long sum = 0;
        left += offset - 1;
        right += offset - 1;

        if(left > right) {
            int temp = left;
            left = right;
            right = temp;
        }

        while(left <= right) {
            if((left & 1) == 1) sum += tree[left++];
            if((right & 1) == 0) sum += tree[right--];
            left /= 2;
            right /= 2;
        }

        return sum;
    }
}


public class Main {
    static int n, q;
    static int[] sequence;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());

        sequence = new int[n];
        IndexedTree indexedTree = new IndexedTree(n);

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        indexedTree.setTree(sequence);

        int x, y, a, b;
        long sum;
        for(int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            sum = indexedTree.getSum(x, y);
            indexedTree.update(a, b);
            sb.append(sum).append("\n");

        }

        System.out.print(sb);

        br.close();
    }
}