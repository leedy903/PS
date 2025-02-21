import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


class IndexedTree {
    int offset;
    int[] tree;

    public IndexedTree(int size) {
        for(offset = 1; offset < size; offset *= 2);
        tree = new int[offset * 2 + 1];
    }

    public void setTree(int[] leaves) {
        int leaf_id;
        for(int i = 0; i < leaves.length; i++) {
            leaf_id = i + offset;
            tree[leaf_id] = leaves[i];
        }

        for(int i = offset - 1; i > 0; i--) {
            tree[i] = getGCDByValue(tree[i * 2], tree[i * 2 + 1]);
        }
        return;
    }
    
    public int getGCDByValue(int a, int b) {
        int r;
        while(b != 0) {
            r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public int getGCDByIndex(int left, int right) {
        int gcd = 0;
        while(left <= right) {
            if((left & 1) == 1) {
                gcd = getGCDByValue(tree[left], gcd);
                left ++;
            }
            if((right & 1) == 0) {
                gcd = getGCDByValue(tree[right], gcd);
                right --;
            }
            left /= 2;
            right /= 2;
        }
        return gcd;
    }

    public void getGCDWithoutOne(int n) {
        int ansGcd = 0;
        int ansValue = -1;
        int leftGcd, rightGcd, midGcd, index;

        rightGcd = getGCDByIndex(offset + 1, n + offset - 1);

        if(ansGcd < rightGcd && (tree[offset] % rightGcd) != 0) {
            ansGcd = rightGcd;
            ansValue = tree[offset];
        }


        for(int i = 1; i < n - 1; i++) {
            index = i + offset;
            leftGcd = getGCDByIndex(offset, index - 1);
            rightGcd = getGCDByIndex(index + 1, n + offset - 1);

            midGcd = Math.max(ansGcd, getGCDByValue(leftGcd, rightGcd));
            if(ansGcd < midGcd && (tree[index] % midGcd) != 0) {
                ansGcd = midGcd;
                ansValue = tree[index];
            }
        }

        leftGcd = getGCDByIndex(offset, n + offset - 2);

        if(ansGcd < leftGcd && (tree[n + offset - 1] % leftGcd != 0)) {
            ansGcd = leftGcd;
            ansValue = tree[n + offset - 1];
        }

        if(ansValue == -1) System.out.println(-1);
        else System.out.println(ansGcd + " " + ansValue);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int [] sequence = new int[n];
        IndexedTree indexedTree = new IndexedTree(n);

        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        indexedTree.setTree(sequence);
        indexedTree.getGCDWithoutOne(n);

        br.close();
    }
}