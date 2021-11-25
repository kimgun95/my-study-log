// 43458 - ������
// �̹����� ����..! �׷��� ������� �κ��� ¥���ϰ� �־���. ���Ӱ� �˰� �� �κ�.
// �� �� �Է� �ޱ�� getline(cin, string) ����..!
// map ����..! find, insert, ���� 
// �Ǽ� ��� ��. cout << fixed �� �Ҽ��� �Ʒ��� �� �ڸ��� �����ϰڴٴ� �ǹ�. 
// cout.precision(x) �� �Ҽ��� x�ڸ� ��ŭ�� ����ϰڴٴ� �ǹ�. 
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
