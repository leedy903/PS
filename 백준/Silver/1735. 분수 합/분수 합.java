import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int numerator1, numerator2, ansNumberator;
        int denominator1, denominator2, ansDemoniator;
        int gcd, lcm;
        st = new StringTokenizer(br.readLine());
        numerator1 = Integer.parseInt(st.nextToken());
        denominator1 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        numerator2 = Integer.parseInt(st.nextToken());
        denominator2 = Integer.parseInt(st.nextToken());

        ansNumberator = numerator1 * denominator2 + numerator2 * denominator1;
        ansDemoniator = denominator1 * denominator2;

        gcd = getGCD(ansNumberator, ansDemoniator);

        System.out.println(ansNumberator / gcd + " " + ansDemoniator / gcd);

        br.close();
    }

    public static int getGCD(int a, int b) {
        int r;
        while(b != 0) {
            r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public static int getLCM(int a, int b) {
        return a * b / getGCD(a, b);
    }
}
