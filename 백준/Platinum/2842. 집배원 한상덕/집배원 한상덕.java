import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

class Point {
    int y;
    int x;

    public Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    static int n;
    static int minHeight = Integer.MAX_VALUE, maxHeight = 0, fatigue = Integer.MAX_VALUE, houseNumber = 0;
    static Point startPoint;
    static char[][] matrix;
    static int[][] heightMatrix;
    static int[] heightArray;
    static HashSet<Integer> heightSet = new HashSet<Integer>();
    static int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dx = {0, -1, -1, -1, 0, 1, 1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        matrix = new char[n][n];
        heightMatrix = new int[n][n];

        for(int i = 0; i < n; i++) {
            matrix[i] = br.readLine().toCharArray();
            for(int j = 0; j < matrix[i].length; j++) {
                if(matrix[i][j] == 'P') {
                    startPoint = new Point(i, j);
                }

                if(matrix[i][j] == 'K') {
                    houseNumber++;
                }
            }
        }

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                int height = Integer.parseInt(st.nextToken());
                heightMatrix[i][j] = height;
                if(matrix[i][j] != '.') {
                    minHeight = Math.min(minHeight, height);
                    maxHeight = Math.max(maxHeight, height);
                }
                heightSet.add(height);
            }
        }

        heightArray = new int[heightSet.size()];

        int idx = 0;
        for(int height: heightSet) {
            heightArray[idx++] = height;
        }

        Arrays.sort(heightArray);
    
        int left = 0, right = 0, minIdx = 0;
        for(int i = 0; i < heightArray.length; i++) {
            if(maxHeight == heightArray[i]) right = i;
            if(minHeight == heightArray[i]) minIdx = i; 
        }

        while(left <= right && left <= minIdx && right < heightArray.length) {
            if(isPossible(heightArray[left], heightArray[right])) {
                fatigue = Math.min(fatigue, heightArray[right] - heightArray[left]);
                left++;
            }
            else {
                right++;
            }
        }

        System.out.println(fatigue);
        br.close();
    }

    public static boolean isPossible(int minHeight, int maxHeight) {
        int houseCount = 0;

        ArrayDeque<Point> deque = new ArrayDeque<Point>();
        boolean[][] visited = new boolean[n][n];

        for(int i = 0; i < n; i++) {
            Arrays.fill(visited[i], false);
        }

        deque.offer(startPoint);
        visited[startPoint.y][startPoint.x] = true;

        while(!deque.isEmpty()) {
            Point now = deque.poll();

            int ny, nx;
            for(int i = 0; i < 8; i++) {
                ny = now.y + dy[i];
                nx = now.x + dx[i];
                if(0 <= ny && ny < n && 0 <= nx && nx < n) {
                    if(!visited[ny][nx] && minHeight <= heightMatrix[ny][nx] && heightMatrix[ny][nx] <= maxHeight) {
                        visited[ny][nx] = true;
                        deque.offer(new Point(ny, nx));

                        if(matrix[ny][nx] == 'K') {
                            houseCount++;
                        }
                    }
                }
            }
        }

        return houseCount == houseNumber;
    }
}