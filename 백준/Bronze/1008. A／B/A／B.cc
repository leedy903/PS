#include <iostream>

using namespace std;

int main() {
    double A, B;

    cout << fixed;
    cout.precision(9);

    cin >> A >> B;
    cout << A / B;

    return 0;
}