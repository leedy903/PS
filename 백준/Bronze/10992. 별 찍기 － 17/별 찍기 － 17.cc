#include <iostream>

using namespace std;

int main(void) {
	int i, j, n = 0;
	
	cin >> n;

	for (i = 0; i < n - 1; i++) {
		for (j = 1; j < n - i; j++) {
			cout << " ";
		}
		for (j = 0; j < i * 2; j++) {
			if (j) cout << " ";
			else cout << "*";
		}
		if (j == 1) cout << "\n";
		else cout << "*\n";
	}
	for (i = 0; i < 2 * n - 1; i++) cout << "*";

	return 0;
}