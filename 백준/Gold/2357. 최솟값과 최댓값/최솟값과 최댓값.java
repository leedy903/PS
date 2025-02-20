import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class IndexedTree {
    int offset;
    int[] min_tree;
    int[] max_tree;

    public IndexedTree(int size) {
        for(offset = 1; offset < size; offset *= 2);
        min_tree = new int[offset * 2];
        max_tree = new int[offset * 2];

        Arrays.fill(min_tree, 1_000_000_000);
    }

    public void setTree(int[] leaves) {
        for(int i = 0; i < leaves.length; i++) {
            min_tree[offset + i] = leaves[i];
            max_tree[offset + i] = leaves[i];
        }

        for(int i = offset - 1; i > 0; i--) {
            min_tree[i] = Math.min(min_tree[i * 2], min_tree[i * 2 + 1]);
            max_tree[i] = Math.max(max_tree[i * 2], max_tree[i * 2 + 1]);
        }
    }

    public int getMin(int left, int right) {
        int min = 1_000_000_000;
        left += offset - 1;
        right += offset - 1;

        while(left <= right) {
            if((left & 1) == 1) min = Math.min(min_tree[left++], min);
            if((right & 1) == 0) min = Math.min(min_tree[right--], min);
            left /= 2;
            right /= 2;
        }

        return min;
    }

    public int getMax(int left, int right) {
        int max = 0;
        left += offset - 1;
        right += offset - 1;

        while(left <= right) {
            if((left & 1) == 1) max = Math.max(max_tree[left++], max);
            if((right & 1) == 0) max = Math.max(max_tree[right--], max);
            left /= 2;
            right /= 2;
        }

        return max;
    }
}


public class Main {
    static int n, m;
    static int[] sequence;
    static IndexedTree indexedTree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        sequence = new int[n];
        indexedTree = new IndexedTree(n);

        for(int i = 0; i < n; i++) {
            sequence[i] = Integer.parseInt(br.readLine());
        }

        indexedTree.setTree(sequence);


        int a, b;
        int max, min;
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            min = indexedTree.getMin(a, b);
            max = indexedTree.getMax(a, b);
            sb.append(min).append(" ").append(max).append("\n");
        }

        System.out.print(sb);
        br.close();    
    }
}