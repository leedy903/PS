import java.util.*;
class Point {
    int y;
    int x;
    public Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

class Solution {
    static Point[][] parent = new Point[51][51];
    static String[][] table = new String[51][51];
    static List<String> ans = new ArrayList<String>();
    
    public String[] solution(String[] commands) {
        
        for(int y = 0; y < 51; y++) {
            for(int x = 0; x < 51; x++) {
                parent[y][x] = new Point(y, x);
            }
        }
        
        for(int y = 0; y < 51; y++) {
            for(int x = 0; x < 51; x++) {
                table[y][x] = "EMPTY";
            }
        }
        
        
        for(String command : commands) {
            String[] cmd = command.split(" "); 
            if(cmd[0].equals("UPDATE") && cmd.length == 4) {
                int r = Integer.parseInt(cmd[1]);
                int c = Integer.parseInt(cmd[2]);
                
                String value = cmd[3];
                
                update(r, c, value);
            }
            else if(cmd[0].equals("UPDATE") && cmd.length == 3) {
                String value1 = cmd[1];
                String value2 = cmd[2];
                
                update(value1, value2);
            }
            else if(cmd[0].equals("MERGE")) {
                int r1 = Integer.parseInt(cmd[1]);
                int c1 = Integer.parseInt(cmd[2]);
                int r2 = Integer.parseInt(cmd[3]);
                int c2 = Integer.parseInt(cmd[4]);
                
                merge(r1, c1, r2, c2);
            }
            else if(cmd[0].equals("UNMERGE")) {
                int r = Integer.parseInt(cmd[1]);
                int c = Integer.parseInt(cmd[2]);
                
                unmerge(r, c);
            }
            else if(cmd[0].equals("PRINT")) {
                int r = Integer.parseInt(cmd[1]);
                int c = Integer.parseInt(cmd[2]);
                
                print(r, c);
            }
        }
        
        String[] answer = ans.toArray(new String[ans.size()]);
        
        return answer;
    }

    
    public static Point find(Point p) {
        if(p != parent[p.y][p.x]) {
            parent[p.y][p.x] = find(parent[p.y][p.x]);
            table[p.y][p.x] = table[parent[p.y][p.x].y][parent[p.y][p.x].x];
        }
        return parent[p.y][p.x];
    }
    
    
    public static void union(Point p1, Point p2) {
        p1 = find(p1);
        p2 = find(p2);
        
        if(table[p1.y][p1.x] == "EMPTY") {
            Point temp = p1;
            p1 = p2;
            p2 = temp;
        }
        
        parent[p2.y][p2.x] = p1;
        table[p2.y][p2.x] = table[p1.y][p1.x];    
    }

    
    public static void update(int r, int c, String value) {
        Point p = find(new Point(r, c));
        table[p.y][p.x] = value;
        return;
    }
    
    
    public static void update(String value1, String value2) {
        for(int y = 1; y < 51; y++) {
            for(int x = 1; x < 51; x++) {
                if(table[y][x].equals(value1)) {
                    table[y][x] = value2;
                }
            }
        }
        return;
    }
    
    
    public static void merge(int r1, int c1, int r2, int c2) {
        union(new Point(r1, c1), new Point(r2, c2));
        return;
    }
    
    
    public static void unmerge(int r, int c) {
        Point p = find(new Point(r, c));;
        String value = table[p.y][p.x];
        
        for(int y = 1; y < 51; y++) {
            for(int x = 1; x < 51; x++) {
                find(new Point(y, x));
            }
        }
        
        for(int y = 1; y < 51; y++) {
            for(int x = 1; x < 51; x++) {
                if(parent[y][x] == p) {
                    parent[y][x] = new Point(y, x);
                    table[y][x] = "EMPTY";
                }
            }
        }
        
        table[r][c] = value;
        
        return;
    }
    
    
    public static void print(int r, int c) {
        Point p = find(new Point(r, c));
        ans.add(table[p.y][p.x]);
        return;
    }
}