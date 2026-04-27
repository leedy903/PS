#include <iostream>

using namespace std;

int main() {
    int h, m, c_time;
    int result;

    cin >> h >> m;
    cin >> c_time;

    result = h * 60 + m + c_time;
    
    h = (result / 60) % 24;
    m = result % 60;

    cout << h << " " << m;

    return 0;
}