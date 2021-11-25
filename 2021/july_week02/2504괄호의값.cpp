// 2504 - ��ȣ�� ��. 
// ���� �����ε�... �������� ���̵� �ʿ��ߴ�.
// ��ȣ�� ���̸� val�� ���Ұ��� ��� �����ְ� ��ȣ�� ���� �� ���ڸ��� �ݴ� ��ȣ��� result�� + ���ְ� �ƴ϶�� �׳� pop�� �����Ѵ�. 
#include <iostream>
#include <stack>
using namespace std;

string s;
stack<int>	 st;
int ans = 0;

int main() {
	// �Է� �ޱ�. 
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
