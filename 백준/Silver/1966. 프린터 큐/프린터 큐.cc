#include <iostream>
#include <queue>

using namespace std;

int main(void) {
	int test_case, N, M, Ipt;
	cin >> test_case;

	for (int i = 0; i < test_case; i++) {
		int count = 0;
		cin >> N >> M;
		queue<pair<int, int>> q;
		priority_queue<int> pq;
		for (int j = 0; j < N; j++) {
			cin >> Ipt;
			q.push({ j, Ipt });
			pq.push(Ipt);
		}
		while (!q.empty()) {
			int index = q.front().first;
			int value = q.front().second;
			q.pop();
			if (value == pq.top()) {
				pq.pop();
				count++;
				if (index == M) {
					cout << count << endl;
					break;
				}
			}
			else {
				q.push({ index, value });
			}
		}
	}
}