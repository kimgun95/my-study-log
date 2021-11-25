// 3425 - ����
// ������, �ǿ����ڸ� pair�� �����Ѵٴ� ���̵� ���� ����. �̰� ���� ���� �Է� ���� �� ���� ��Ȥ�̾���. 
#include <iostream>
#include <vector>
#include <stack>
#include <cstdlib> //abs �Լ� ��� ����. 
using namespace std;

typedef pair<string, int> psi; //������, �ǿ����� ���� �ֱ� ����. 
string cmd;

int main() {
	// cmd�� QUIT�� �Էµ� �� ���� �ݺ�. 
	while(true) {
		vector<psi> sys;
		// Ŀ�ǵ� �Է� �ޱ�. END�� Ŀ�ǵ� �Է� ����. 
		while (cin >> cmd) {
			if (cmd == "QUIT") return 0;
			if (cmd == "END") break;
			
			int operand = 0;
			if (cmd == "NUM") {
				cin >> operand;
			}
			// ������, �ǿ����� pair�� vector�� push_back 
			sys.push_back(psi(cmd, operand));
		}
		// ���� Ƚ�� �Է� �ޱ�.
		int cnt;
		cin >> cnt;
		// ������ ���� �Է� �ޱ�. 
		long test[cnt];
		for (int i = 0; i < cnt; i++) {
			cin >> test[i];
		}
		
		// ��� ����.
		for (int i = 0; i < cnt; i++) {
			// ����� ù ���� stack�� push 
			stack<long> s;
			s.push(test[i]);
			// ��� ����� error���� �Ǵ��ϴ� ����. 
			int error = 0;
			// vector�� size��ŭ ����. 
			for (int j = 0; j < sys.size(); j++) {
				if (sys[j].first == "NUM") {
					if (sys[j].second < 0 || sys[j].second > 1000000000) {
						error = 1;
						break;
					}
					s.push(sys[j].second);
				} else if (sys[j].first == "POP") {
					if (s.empty()) {
						error = 1;
						break;
					}
					s.pop();
				} else if (sys[j].first == "INV") {
					if (s.empty()) {
						error = 1;
						break;
					}
					long num = s.top() * -1;
					s.pop();
					s.push(num);
				} else if (sys[j].first == "DUP") {
					if (s.empty()) {
						error = 1;
						break;
					}
					long num = s.top();
					s.push(num);
				} else if (sys[j].first == "SWP") {
					if (s.size() < 2) {
						error = 1;
						break;
					}
					long num1 = s.top();
					s.pop();
					long num2 = s.top();
					s.pop();
					s.push(num1);
					s.push(num2);
				} else if (sys[j].first == "ADD") {
					if (s.size() < 2) {
						error = 1;
						break;
					}
					long num1 = s.top();
					s.pop();
					long num2 = s.top();
					s.pop();
					if (abs(num1 + num2) > 1000000000) {
						error = 1;
						break;
					}
					s.push(num1 + num2);
				} else if (sys[j].first == "SUB") {
					if (s.size() < 2) {
						error = 1;
						break;
					}
					long num1 = s.top();
					s.pop();
					long num2 = s.top();
					s.pop();
					if (abs(num2 - num1) > 1000000000) {
						error = 1;
						break;
					}
					s.push(num2 - num1);
				} else if (sys[j].first == "MUL") {
					if (s.size() < 2) {
						error = 1;
						break;
					}
					long num1 = s.top();
					s.pop();
					long num2 = s.top();
					s.pop();
					if (abs(num2 * num1) > 1000000000) {
						error = 1;
						break;
					}
					s.push(num2 * num1);
				} else if (sys[j].first == "DIV") {
					if (s.size() < 2) {
						error = 1;
						break;
					}
					long num1 = s.top();
					s.pop();
					if (num1 == 0) {
						error = 1;
						break;
					}
					long num2 = s.top();
					s.pop();
					long ans = abs(num2) / abs(num1);
					if (num1 < 0 != num2 < 0) ans *= -1;
					if (abs(ans) > 1000000000) {
						error = 1;
						break;
					}
					s.push(ans);
				} else if (sys[j].first == "MOD") {
					if (s.size() < 2) {
						error = 1;
						break;
					}
					long num1 = s.top();
					s.pop();
					if (num1 == 0) {
						error = 1;
						break;
					}
					long num2 = s.top();
					s.pop();
					long ans = abs(num2) % abs(num1);
					if (num2 < 0) ans *= -1;
					if (abs(ans) > 1000000000) {
						error = 1;
						break;
					}
					s.push(ans);
				} else {
					error = 1;
					break;
				}
			}
			// ���� ��� ���. error�� ERROR�� ���. 
			if (s.size() == 1 && error == 0) {
				cout << s.top() << endl;
			} else {
				cout << "ERROR" << endl;
			}
		}
		// ������ �� �� �� ���. �̰� ������ ��� ���� ������� ��� �� ����; 
	 	cout << endl;
	}	
	return 0;
}
