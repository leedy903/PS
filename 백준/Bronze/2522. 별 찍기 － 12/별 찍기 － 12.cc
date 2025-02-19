#include <iostream>

using namespace std;

int main(void) {
	int i = 0, j = 0, n = 0;

	cin >> n;

	for (i = 1; i < 2 * n + 1; i++) {
		for (j = 0; i < n ? j < n - i : j < i - n; j++)
		{
			cout << " ";
		}
		for (j = 0; i < n ? j < i : j < 2 * n - i; j++) {
			cout << "*";
		}
		cout << endl;
	}
	return 0;
}