import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[][] meetings = new int[n][2];
        List<int[]> allocated_meetings = new ArrayList<int[]>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            meetings[i][0] = Integer.parseInt(st.nextToken());
            meetings[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(meetings, new Comparator<int[]>() {
            @Override
            public int compare(int[] s1, int[] s2) {
                if (s1[1] > s2[1]) {
                    
                    return 1;
                }
                else if (s1[1] == s2[1]) {
                    if (s1[0] > s2[0]) {
                        return 1;
                    }
                    else {
                        return -1;
                    }
                }
                else {
                    return -1;
                }
            }
        });

        allocated_meetings.add(meetings[0]);

        for (int i = 1; i < meetings.length; i++) {
            if (allocated_meetings.get(allocated_meetings.size() - 1)[1] <= meetings[i][0]) {
                allocated_meetings.add(meetings[i]);
            }
        }
        System.out.println(allocated_meetings.size());
        br.close();
    }
}