#include <iostream>
#include <string>

using namespace std;

int matrix[20][20];
int r, c;
int max_count = 0;
bool container[26] = {false, };
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, -1, 0, 1};

void dfs(bool container[26], int depth, int y, int x){

    max_count = max(max_count, depth);
    int now = matrix[y][x];
    container[now] = true;

    for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if(0 <= ny && ny < r && 0 <= nx && nx < c) {
            int alphabet = matrix[ny][nx];
            if(!container[alphabet]) {
                container[alphabet] = true;
                dfs(container, depth + 1, ny, nx);
                container[alphabet] = false;
            }
        }
    }
}

int main() {
    cin >> r >> c;
    for(int i = 0; i < r; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < c; j++) {
            matrix[i][j] = int(s[j]) - int('A');
        }
    }

    dfs(container, 1, 0, 0);

    cout << max_count;

    return 0;
}