#include<iostream>

using namespace std;

int n, m;
int sequence[2000];
int questions[1000000][2];
int dp[2000][2000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> sequence[i];
    }

    cin >> m;

    for(int i = 0; i < m; i++) {
        int s, e;
        cin >> s >> e;
        questions[i][0] = s - 1;
        questions[i][1] = e - 1;
    }

    for(int i = 0; i < n; i++) {
        dp[i][i] = 1;
        if(i < n - 1 && sequence[i] == sequence[i + 1]) {
            dp[i][i + 1] = 1;
        }
    }

    for(int alpha = 2; alpha < n; alpha++) {
        for(int i = 0; i < n - alpha; i++) {
            int j = i + alpha;
            if(dp[i + 1][j - 1] == 1 && sequence[i] == sequence[j]) {
                dp[i][j] = 1;
            }
        }
    }

    for(int i = 0; i < m; i++) {
        int s = questions[i][0];
        int e = questions[i][1];
        cout << dp[s][e] << '\n';
    }

    return 0;
}