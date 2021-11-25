// 3425 - 고스택
// 연산자, 피연산자를 pair로 저장한다는 아이디어가 가장 컸음. 이게 없을 때는 입력 받을 때 부터 곤혹이었음. 
#include <iostream>
#include <vector>
#include <stack>
#include <cstdlib> //abs 함수 사용 위함. 
using namespace std;

typedef pair<string, int> psi; //연산자, 피연산자 쌍을 넣기 위함. 
string cmd;

int main() {
	// cmd에 QUIT가 입력될 때 까지 반복. 
	while(true) {
		vector<psi> sys;
		// 커맨드 입력 받기. END로 커맨드 입력 종료. 
		while (cin >> cmd) {
			if (cmd == "QUIT") return 0;
			if (cmd == "END") break;
			
			int operand = 0;
			if (cmd == "NUM") {
				cin >> operand;
			}
			// 연산자, 피연산자 pair를 vector에 push_back 
			sys.push_back(psi(cmd, operand));
		}
		// 수행 횟수 입력 받기.
		int cnt;
		cin >> cnt;
		// 수행할 숫자 입력 받기. 
		long test[cnt];
		for (int i = 0; i < cnt; i++) {
			cin >> test[i];
		}
		
		// 계산 수행.
		for (int i = 0; i < cnt; i++) {
			// 계산할 첫 숫자 stack에 push 
			stack<long> s;
			s.push(test[i]);
			// 계산 결과가 error인지 판단하는 변수. 
			int error = 0;
			// vector에 size만큼 진행. 
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
			// 수행 결과 출력. error는 ERROR로 출력. 
			if (s.size() == 1 && error == 0) {
				cout << s.top() << endl;
			} else {
				cout << "ERROR" << endl;
			}
		}
		// 마지막 한 줄 더 출력. 이것 때문에 출력 형식 오류라고 결과 봄 ㅎㅎ; 
	 	cout << endl;
	}	
	return 0;
}
