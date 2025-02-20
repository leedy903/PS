#include <iostream>

using namespace std;

int n, m;
int truth[51];
int parent[51];
int party[51][51];

int FindParent(int x) {
    if(x != parent[x])
        parent[x] = FindParent(parent[x]);
    return parent[x];
}

void Union(int a, int b) {
    a = FindParent(a);
    b = FindParent(b);

    if(a < b) parent[b] = a;
    else parent[a] = b;
}


int main() {
    int truth_len = 0;
    int count = 0;

    for(int i = 0; i < 51; i++) {
        parent[i] = i;
    }
    
    cin >> n >> m;
    cin >> truth_len;
    
    for(int i = 0; i < truth_len; i++) {
        cin >> truth[i];
    }

    for(int i = 0; i < truth_len; i++) {
        parent[truth[i]] = 0;
    }

    for(int i = 0; i < m; i++) {
        cin >> party[i][0];

        for(int j = 0; j < party[i][0]; j++) {
            cin >> party[i][j + 1];
        }

        for(int j = 1; j < party[i][0]; j++) {
            Union(party[i][j], party[i][j + 1]);
        }
    }
    
    for(int i = 1; i < n + 1; i++) {
        FindParent(i);
    }

    for(int i = 0; i < m; i++) {
        bool isOkayToSay = true;
        for(int j = 0; j < party[i][0]; j++) {
            if(parent[party[i][j + 1]] == 0) {
                isOkayToSay = false;
                break;
            }
        }
        if(isOkayToSay) count ++;
    }

    cout << count;

    return 0;
}