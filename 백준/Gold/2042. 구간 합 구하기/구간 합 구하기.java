import java.io.*;
import java.util.*;

class IndexedTree {
    int offset;
    long[] tree;

    public IndexedTree(int size) {
        for (offset = 1; offset < size; offset *= 2);
        tree = new long[offset * 2 + 2];
    }

    public void setTree(long[] leaves) {
        for (int i = 0; i < leaves.length; i++) {
            tree[i + offset] = leaves[i];
        }

        for (int i = offset - 1; i > 0; i--) {
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }
    }

    public void updateTree(int id, long value) {
        int tid = id + offset - 1;
        tree[tid] = value;
        while(tid > 1) {
            tid /= 2;
            tree[tid] = tree[tid * 2] + tree[tid * 2 + 1];
        }
    }

    public long getSum(int left, int right) {
        long sum = 0;
        left += offset - 1;
        right += offset - 1;
        while(left <= right) {
            if ((left & 1) == 1) sum += tree[left++];
            if ((right & 1) == 0) sum += tree[right--];
            left /= 2;
            right /= 2;
        }
        return sum;
    }
}

public class Main {

    static int n, m, k;
    static long[] numbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        numbers = new long[n];

        for (int i = 0; i < n; i ++) {
            numbers[i] = Long.parseLong(br.readLine());
        }

        IndexedTree indexedTree = new IndexedTree(n);
        indexedTree.setTree(numbers);

        for (int i = 0; i < m + k; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            if (command == 1) {
                int id = Integer.parseInt(st.nextToken());
                long value = Long.parseLong(st.nextToken());
                indexedTree.updateTree(id, value);
            }
            else {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());
                sb.append(indexedTree.getSum(left, right)).append("\n");
            }
        }

        System.out.print(sb);
        br.close();
    }
}