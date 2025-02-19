#include <iostream>
#include <queue>

using namespace std;

int main(void) {
	int N = 0, K = 0;
	int i = 0;

	queue<int> q;
	
	cin >> N >> K;

	for (i = 0; i < N; i++) q.push(i + 1);

	cout << '<';
	while (true) {
		for (i = 1; i < K; ++i) {
			q.push(q.front());
			q.pop();
		}
		cout << q.front();
		q.pop();
		if (!q.empty()) {
			cout << ", " ;
		}
		else {
			cout << '>';
			break;
		}
	}

	return 0;
}