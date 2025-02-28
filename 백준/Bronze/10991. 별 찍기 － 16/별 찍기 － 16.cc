#include <iostream>
using namespace std;
int N = 0;
void dfs(int n) {
	int i, j;
	if (n > 0) {
		for (i = 0; i < n - 1; i++) {
			cout << " ";
		}
		for (j = 0; j < 2 * (N - n + 1); j++) {
			if (j % 2) cout << " ";
			else cout << "*";
		}
		cout << endl;
		dfs(--n);
	}
	else return;
}
int main(void) {
	cin >> N;
	dfs(N);
	return 0;
}