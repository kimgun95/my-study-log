// 6416 - Ʈ���ΰ�?
// ���� Ǯ���� �ڵ�ε� 50%���� �����߾��µ� �� Ʋ�ȴ��� ���ذ� ���� �ʴ´�... �� �ǰ� ū ������ ���޾ƿͼ� �׷��ǰ�..? �ͱ⵵ ������ �𸣰ڴ�.
// ��带 �����Ҷ� �迭�� �̿��ؼ� check�߾��µ� �׳� set�� �̿��ؼ� �ߺ� ���� �˾Ƽ� ���� �ȵǰ� �ϴ� �� ����� Ǯ�̵� ���� �� ����. 
#include <iostream>
#include <vector>
#include <set>
using namespace std;

typedef pair<int, int> pii;

int a, b; // �Է� ���� 
int kase = 1;  // case ǥ�� ��. 
vector<pii> v; // ���� ���� ����. 
set<int> s; // ��� ���� set. �ߺ��� �˾Ƽ� �ɷ��ִ� ���� �ڷ���. 

int main() {
	
	while(true) {
		cin >> a >> b;
		// ���� ����. 
		if (a == -1 && b == -1) break;
		if (a == 0 && b == 0) {
			// Ʈ������ �˻�.
			if (v.size() + 1 == s.size() || v.size() == 0) cout << "Case " << kase << " is a tree.\n";
			else cout << "Case " << kase << " is not a tree.\n";
			kase++;
			v.clear();
			s.clear();
		} else {
			// ��� �߰�. 
			v.push_back(pii(a, b));
			s.insert(a);
			s.insert(b);
		}
	}	

	
	return 0;
} 
