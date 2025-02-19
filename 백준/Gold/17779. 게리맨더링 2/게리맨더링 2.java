import java.io.*;
import java.util.*;

class Point {
    int y;
    int x;
    Point (int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {
    public static int n, total;
    public static int answer = Integer.MAX_VALUE;
    public static int [][] matrix;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        matrix = new int[n][n];

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int population = Integer.parseInt(st.nextToken());
                matrix[i][j] = population;
                total += population;
            }
        }

        for (int y = 1; y < n - 2; y++) {
            for (int x = 0; x < n - 2; x++) {
                Point[] points = {new Point(y, x), new Point(y - 1, x + 1), new Point(y, x + 2), new Point(y + 1, x + 1)};
                dfs(points, getNDistricts(points));
            }
        }

        System.out.println(answer);
        br.close();
    }

    // [W, N, E, S]
    public static void dfs(Point[] points, int[] districts) {
        Point[] nPoints;

        int max = 0, min = Integer.MAX_VALUE;

        for (int district : districts) {
            max = Math.max(max, district);
            min = Math.min(min, district);
        }

        answer = Math.min(answer, max - min);

        // 오른쪽 위로 확장
        nPoints = new Point[points.length];
        for (int i = 0; i < points.length; i++) {
            nPoints[i] = new Point(points[i].y, points[i].x);
        }
        nPoints[1].y -= 1;
        nPoints[1].x += 1;
        nPoints[2].y -= 1;
        nPoints[2].x += 1;
        if (0 <= nPoints[1].y && nPoints[2].x < n) {
            dfs(nPoints, getNDistricts(nPoints));
        } 

        // 오른쪽 아래로 확장
        nPoints = new Point[points.length];
        for (int i = 0; i < points.length; i++) {
            nPoints[i] = new Point(points[i].y, points[i].x);
        }
        nPoints[2].y += 1;
        nPoints[2].x += 1;
        nPoints[3].y += 1;
        nPoints[3].x += 1;
        if (nPoints[2].x < n && nPoints[3].y < n) {
            dfs(nPoints, getNDistricts(nPoints));
        } 
    }

    public static int[] getNDistricts(Point[] points) {
        int[] nDistricts = new int[5];
        Point west, north, east, south;

        west = points[0];
        north = points[1];
        east = points[2];
        south = points[3];

        nDistricts[0] = getDistrict1(west, north);
        nDistricts[1] = getDistrict2(north, east);
        nDistricts[2] = getDistrict3(west, south);
        nDistricts[3] = getDistrict4(south, east);
        nDistricts[4] = total - (nDistricts[0] + nDistricts[1] + nDistricts[2] + nDistricts[3]);

        return nDistricts;
    }

    public static int getDistrict1(Point west, Point north) {
        int step = 1, size = 0;
        for (int i = west.y - 1; i >= 0; i--) {
            for (int j = 0; j < Math.min(north.x + 1, west.x + step); j++) {
                size += matrix[i][j];
            }
            step++;
        }
        return size;
    }

    public static int getDistrict2(Point north, Point east) {
        int step = 0, size = 0;
        for (int i = east.y; i >= 0; i--) {
            for (int j = n - 1; j >= Math.max(north.x + 1, east.x + 1 - step); j--) {
                size += matrix[i][j];
            }
            step++;
        }
        return size;
    }

    public static int getDistrict3(Point west, Point south) {
        int step = 0, size = 0;
        for (int i = west.y; i < n; i++) {
            for (int j = 0; j < Math.min(west.x + step, south.x); j++) {
                size += matrix[i][j];
            }
            step++;
        }
        return size;
    }

    public static int getDistrict4(Point south, Point east) {
        int step = 0, size = 0;
        for (int i = east.y + 1; i < n; i++) {
            for (int j = Math.max(east.x - step, south.x); j < n; j++) {
                size += matrix[i][j];
            }
            step++;
        }
        return size;
    }
}
