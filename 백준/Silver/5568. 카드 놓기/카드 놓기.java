import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    static int n, k;
    static boolean[] visited;
    static HashSet<String> cardSet;
    static String [] cards;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        visited = new boolean[n];
        cardSet = new HashSet<String>();
        cards = new String[n];

        for(int i = 0; i < n; i++) {
            cards[i] = br.readLine();
        }

        permuation("", 0);
        System.out.println(cardSet.size());

        br.close();
    }
    public static void permuation(String num, int count) {
        if(count == k) {
            cardSet.add(num);
            return;
        }

        for(int i = 0; i < n; i++) {
            if(visited[i] == false) {
                visited[i] = true;
                permuation(num + cards[i], count + 1);
                visited[i] = false;
            }
        }
    }
}
