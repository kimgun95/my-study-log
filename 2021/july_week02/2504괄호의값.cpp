// 2504 - 괄호의 값. 
// 스택 문제인데... 생각보다 아이디어가 필요했다.
// 괄호가 쌓이면 val에 곱할값을 계속 곱해주고 괄호를 닫을 때 열자마자 닫는 괄호라면 result를 + 해주고 아니라면 그냥 pop만 진행한다. 
#include <iostream>
#include <stack>
using namespace std;

string s;
stack<int>	 st;
int ans = 0;

int main() {
	// 입력 받기. 
	cin >> s;
	
	int val = 1;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '(') {
			val *= 2;
			st.push(s[i]);
		} else if (s[i] == '[') {
			val *= 3;
			st.push(s[i]);
		} else if (s[i] == ')') {
			if (st.empty() || st.top() != '(') {
				cout << 0;
				exit(0);
			} else if (s[i - 1] == '(') {
				ans += val;
			} 
			val /= 2;
			st.pop();
		} else if (s[i] == ']') {
			if (st.empty() || st.top() != '[') {
				cout << 0;
				exit(0);
			} else if (s[i - 1] == '[') {
				ans += val;
			} 
			val /= 3;
			st.pop();
		}
	}
	
	if (!st.empty()) {
		cout << 0;
	} else {
		cout << ans;
	}
	
	
	return 0;
} 
