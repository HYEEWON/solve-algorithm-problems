#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
// 7, 3, 9 -> 2, 1
// 5, 10, 1, 1, 20, 1 -> 1, 3, 2
// 20, 1, 1, 5
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> day(speeds.size());
    stack<int> st;
    queue<int> q;

    for (int i = 0; i < speeds.size(); ++i) {
        day[i] = int((100 - progresses[i]) / speeds[i]);
        if ((100 - progresses[i]) % speeds[i] != 0) day[i] += 1;
    }
    
    for (int i = 0; i < speeds.size(); ++i) {
        while (!q.empty() && day[i] > day[q.front()]) {
            int front = q.front();
            answer.push_back(i - front);
            while (!q.empty()) q.pop();
        }
        q.push(i);      
    }
    answer.push_back(q.size());
    return answer;
}

int main() {

    vector<int>p = { 93, 30, 55 };
    vector<int>v = { 1, 30, 5 };
    vector<int> ans = solution(p, v);
    cout << "main: ";
    for (int i = 0; i < ans.size(); ++i) {
        cout << ans[i] << ' ';
    }
    return 0;
}