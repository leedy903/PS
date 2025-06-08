import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class IndexedTree {
    int offset = 1;
    int [] tree;

    public IndexedTree(int size) {
        while(offset < size) offset *= 2;
        tree = new int[offset * 2 + 1];
    }

    public void setTree(int[] leaves) {
        for (int i = 0; i < leaves.length; i++) {
            if (leaves[i] == 0) {
                tree[offset + i] = 0;
            }
            else {
                tree[offset + i] = leaves[i] > 0 ? 1 : -1;
            }
        }

        for (int i = offset - 1; i > 0; i--) {
            tree[i] = tree[i * 2] * tree[i * 2 + 1];
        }
    }

    public void update(int index, int value) {
        if (value == 0) {
            tree[offset + index - 1] = 0;
        }
        else {
            tree[offset + index - 1] = value > 0 ? 1 : -1;
        }

        for (int i = (offset + index - 1) / 2; i > 0; i /= 2) {
            tree[i] = tree[i * 2] * tree[i * 2 + 1];
        }
    }

    public int getResult(int start, int end) {
        int result = 1;
        start += offset - 1;
        end += offset - 1;

        while(start <= end) {
            if ((start & 1) == 1) result *= tree[start++];
            if ((end & 1) == 0) result *= tree[end--];
            start /= 2;
            end /= 2;
        }

        return result;
    }

}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        String input = "";
        while ((input = br.readLine()) != null) {
            int N, K;
            st = new StringTokenizer(input);
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            IndexedTree tree = new IndexedTree(N);
            int[] leaves = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                leaves[i] = Integer.parseInt(st.nextToken());
            }

            tree.setTree(leaves);

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                String cmd = st.nextToken();
                if (cmd.equals("C")) {
                    int index = Integer.parseInt(st.nextToken());
                    int value = Integer.parseInt(st.nextToken());
                    tree.update(index, value);
                } else if (cmd.equals("P")) {
                    int start = Integer.parseInt(st.nextToken());
                    int end = Integer.parseInt(st.nextToken());
                    int result = tree.getResult(start, end);
                    if (result > 0) {
                        sb.append("+");
                    } else if (result < 0) {
                        sb.append("-");
                    } else {
                        sb.append("0");
                    }
                }
            }
            sb.append("\n");
        }

        System.out.println(sb);

        br.close();
    }
}