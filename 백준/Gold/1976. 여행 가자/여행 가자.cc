#include<iostream>
#include<algorithm>

using namespace std;

int n, m;
int parents[200];
int plan[1000];

int FindParent(int x) {
    if (parents[x] != x) {
        parents[x] = FindParent(parents[x]);
    }
    return parents[x];
}


void Union(int x, int y) {
    int parent_x = FindParent(x);
    int parent_y = FindParent(y);

    if(parent_x < parent_y) {
        parents[parent_y] = parent_x;
    }
    else {
        parents[parent_x] = parent_y;
    }
}


int main() {
    int x;
    cin >> n >> m;

    for(int i = 0; i < n; i++) {
        parents[i] = i;
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> x;
            if(x == 1) {
                Union(i, j);
            }
        }
    }

    for(int i = 0; i < m; i++) {
        cin >> plan[i];
    }

    bool isPossible = true;
    int root = FindParent(plan[0] - 1);
    for(int i = 1; i < m; i++) {
        if(root != FindParent(plan[i] - 1)) {
            isPossible = false;
            break;
        }
    }

    if(isPossible) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }

    return 0;
}