#include <string>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

long long solution(int n, vector<int> works) {
    
    long long answer = 0;
    priority_queue<int, vector<int>> heap;
    vector<int>::iterator iter;
    
    for(iter = works.begin(); iter != works.end(); iter++) {
        heap.push(*iter);
    }
    
    for(; n != 0 && !heap.empty(); n--) {
        int work = heap.top();
        heap.pop();
        if(work > 0) {
            heap.push(work - 1);
        }
    }
    
    while(!heap.empty()) {
        int remain = heap.top();
        heap.pop();
        answer += pow(remain, 2);
    }
    
    
    return answer;
}