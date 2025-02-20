#include <iostream>

using namespace std;

int self_number[10000] = {0, };

int dnContructor(int n) {
    int next_n = n;
    while(n > 0) {
        next_n += n % 10;
        n /= 10;
    }
    return next_n;
}

int main() {

    for(int i = 1; i < 10000; i++) {
        int n = i;
        while((n = dnContructor(n)) < 10000) {
            self_number[n] = n;
        }        
    }

    for(int i = 1; i < 10000; i++) {
        if(self_number[i] == 0) {
            cout << i << '\n';
        }
    }

    return 0;
}