import java.io.*;
import java.util.*;

class Player implements Comparable<Player> {
    int id, speed;

    public Player(int id, int speed) {
        this.id = id;
        this.speed = speed;
    }

    @Override
    public int compareTo(Player p) {
        return p.speed - this.speed;
    }
}

class IndexedTree {
    int offset;
    int[] tree;

    IndexedTree(int size) {
        for(offset = 1; offset < size; offset *= 2);
        tree = new int[offset * 2 + 2];
    }

    public void setTree() {
        Arrays.fill(tree, 0);
    }

    public void updateTree(int id) {
        int tid = id + offset;
        tree[tid] = 1;
        while (tid > 1) {
            tid /= 2;
            tree[tid] = tree[tid * 2] + tree[tid * 2 + 1];
        }
    }

    public int getSum(int id) {
        int sum = 0;
        int left = offset;
        int right = offset + id;

        while (left <= right) {
            if ((left & 1) == 1) sum += tree[left++];
            if ((right & 1) == 0) sum += tree[right--];
            left /= 2;
            right /= 2;
        }

        return sum;
    }
}

public class Main {
    static int n;
    static int[] ranks;
    static Player[] players;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        ranks = new int[n];
        players = new Player[n];

        for (int i = 0; i < n; i++) {
            int speed = Integer.parseInt(br.readLine());
            players[i] = new Player(i, speed);
        }

        Arrays.sort(players);

        IndexedTree indexedTree = new IndexedTree(n);
        indexedTree.setTree();

        for (Player player : players) {
            indexedTree.updateTree(player.id);
            ranks[player.id] = indexedTree.getSum(player.id);
        }

        for (int rank : ranks) {
            sb.append(rank).append("\n");
        }

        System.out.print(sb);
        br.close();
    }
}