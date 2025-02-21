#include <iostream>

using namespace std;

int main(void) {
	int i, j, k, n = 0;

	cin >> n;

	for (i = 1; i < n + 1; i++) {
		for (j = 0; j < n - i; j++) {
			cout << " ";
		}
		for (k = 0; k < i * 2 - 1; k++) {
			cout << "*";
		}
		cout << endl;
	}
}