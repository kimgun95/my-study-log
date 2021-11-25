// 43458 - 생태학
// 이번에도 성공..! 그러나 어려웠던 부분은 짜잘하게 있었다. 새롭게 알게 된 부분.
// 한 줄 입력 받기는 getline(cin, string) 으로..!
// map 사용법..! find, insert, 수정 
// 실수 출력 법. cout << fixed 는 소수점 아래를 몇 자리로 고정하겠다는 의미. 
// cout.precision(x) 는 소수점 x자리 만큼을 출력하겠다는 의미. 
#include <iostream>
#include <map>
using namespace std;

string s;
map<string, int> m;
int cnt = 0;

int main() {
		
	while(true) {
		getline(cin, s);
		if (cin.eof()) break;
		if (m.find(s) == m.end()) m.insert({s, 1});
		else {
			int num = m[s];
			m[s] = num + 1;
		}
		cnt++;
	}
	
	cout << fixed;
	cout.precision(4);
	for (auto i : m) 
		cout << i.first << " " << (i.second * 100)/(double)cnt << "\n";

	return 0;
} 
