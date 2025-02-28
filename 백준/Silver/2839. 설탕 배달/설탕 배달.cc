#include <iostream>

using namespace std;

int main() {
    int sugar;
    int five_kilo = 0;
    int three_kilo = 0;
    int remain = 0;

    cin >> sugar;
    
    for(five_kilo = sugar / 5; five_kilo > 0; five_kilo--) {
        remain = sugar - five_kilo * 5;
        three_kilo = remain / 3;
        if(remain % 3 == 0) {
            break;
        }
    }

    if(five_kilo > 0) {
        cout << five_kilo + three_kilo;
    }
    else if (sugar % 3 == 0) {
            cout << sugar / 3;
    }
    else {
        cout << -1;
    }


    return 0;
}