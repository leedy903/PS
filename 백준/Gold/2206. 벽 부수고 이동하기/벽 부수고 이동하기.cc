#include<iostream>
#include<algorithm>
#include<queue>
#include<string>

using namespace std;

int n, m;
int matrix[1000][1000];
int visit[1000][1000][2];

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, -1, 0, 1};

typedef struct Position{
    int y;
    int x;
    int block;
} Pos;


int BFS() {
    queue<Pos> q;
    // y, x, block
    Pos p = {0, 0, 1};

    q.push(p);
    visit[0][0][0] = 1;
    visit[0][0][1] = 1;

    while(!q.empty()) {
        Pos cur = q.front();
        int y = cur.y;
        int x = cur.x;
        int block = cur.block;
        q.pop();

        if(y == n - 1 && x == m - 1) {
            return visit[y][x][block];
        }

        for(int dir = 0; dir < 4; dir++) {
            int ny = y + dy[dir];
            int nx = x + dx[dir];

            if(0 <= ny && ny < n && 0 <= nx && nx < m) {
                if(matrix[ny][nx] == 0 && visit[ny][nx][block] == 0) {
                    visit[ny][nx][block] = visit[y][x][block] + 1;
                    Pos next = {ny, nx, block};
                    q.push(next);
                }
                if(matrix[ny][nx] == 1 && block > 0) {
                    visit[ny][nx][block - 1] = visit[y][x][block] + 1;
                    Pos next = {ny, nx, block - 1};
                    q.push(next);
                }
            }
        }
    }
    return -1;
}


int main() {

    cin >> n >> m;
    
    for(int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < m; j++) {
            matrix[i][j] = (int)s[j] - '0';
        }
    }

    cout << BFS();

    return 0;
}