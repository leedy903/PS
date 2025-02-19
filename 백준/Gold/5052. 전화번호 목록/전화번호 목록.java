import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class Node {
    Map<Character, Node> children = new HashMap<Character, Node>();
    boolean isTerminal = false;
}

class Trie {
    Node root;

    Trie() {
        root = new Node();
    }

    void insert(String word) {
        Node cur = this.root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new Node());
            }
            cur = cur.children.get(c);
        }
        cur.isTerminal = true;
    }

    boolean isConsistent(String word) {
        Node cur = this.root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (cur.isTerminal) return false;
            cur = cur.children.get(c);
        }
        return true;
    }
}


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int test_case = 0; test_case < t; test_case++) {
            Trie trie = new Trie();
            String answer = "YES";

            int n = Integer.parseInt(br.readLine());
            String[] phoneNumbers = new String[n];

            for (int i = 0; i < n; i++) {
                String phoneNumber = br.readLine();
                phoneNumbers[i] = phoneNumber;
                trie.insert(phoneNumber);
            }

            for (int i = 0; i < n; i++) {
                String phoneNumber = phoneNumbers[i];
                if (!trie.isConsistent(phoneNumber)) {
                    answer = "NO";
                    break;
                }
            }
            sb.append(answer).append("\n");
        }
        System.out.print(sb);
        br.close();
    }
}