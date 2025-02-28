import java.io.*;
import java.util.*;

class IndexedTree {
    int offset;
    int[] tree;
    IndexedTree(int size) {
        for(offset = 1; offset < size; offset *= 2);
        tree = new int[offset * 2 + 2];
    }

    public void updateTree(int id, int value) {
        int tid = id + offset - 1;
        tree[tid] += value;
        while(tid > 1) {
            tid /= 2;
            tree[tid] = tree[tid * 2] + tree[tid * 2 + 1];
        }
    }

    public int getSum(int id) {
        int sum = 0;
        int left = offset;
        int right = id + offset - 1;

        while(left <= right) {
            if ((left & 1) == 1) sum += tree[left++];
            if ((right & 1) == 0) sum += tree[right--];
            left /= 2;
            right /= 2;
        }
        return sum;
    }

    public int searchId(int rank) {
        int id = 1;
        int left = 1;
        int right = tree.length - offset - 2;
        while(left <= right) {
            int mid = (left + right) / 2;
            int sum = getSum(mid);
            if (sum >= rank) {
                id = mid;
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return id;
    }
}


public class Main {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        IndexedTree indexedTree = new IndexedTree(1_000_000);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            if (command == 1) {
                int rank = Integer.parseInt(st.nextToken());
                int flavorId = indexedTree.searchId(rank);
                indexedTree.updateTree(flavorId, -1);
                sb.append(flavorId).append("\n");
            }
            else if (command == 2) {
                int flavorId = Integer.parseInt(st.nextToken());
                int count = Integer.parseInt(st.nextToken());
                indexedTree.updateTree(flavorId, count);
            }
        }
        System.out.print(sb);
        br.close();
    }
}