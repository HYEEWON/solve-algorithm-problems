#include <iostream>
#include <deque>
#include <stack>
#include <string>
#include <vector>

using namespace std;

/*vector<int> solution(vector<int> prices) {
    vector<int> answer;  
    for (int i = 0; i < prices.size(); ++i) {
        deque<int> dq;
        for (int j = i+1; j < prices.size(); j++) {
            if (prices[i] <= prices[j]) dq.push_back(prices[j]);
            else {
                dq.push_back(0);
                break;
            }
        }       
        answer.push_back(dq.size());
    }
    return answer;
}*/

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size());
    stack<int> s;
    s.push(0);
    for (int i = 1; i < prices.size(); ++i) {
        while (!s.empty() && prices[s.top()] > prices[i]) {
            int top = s.top(); //½Ã°£
            s.pop();
            answer[top] = i - top;
        }
        s.push(i);
    }
    while (!s.empty()) {
        int top = s.top();
        s.pop();
        answer[top] = prices.size() - top - 1;
    }
    return answer;
}

int main() {
    vector<int>p = { 1, 2, 3, 2, 3 };
    vector<int> ans = solution(p);
    for (int i = 0; i < ans.size(); ++i) {
        cout << ans[i] << ' ';
    }
	return 0;
}