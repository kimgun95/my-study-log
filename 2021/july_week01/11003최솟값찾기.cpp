// 11003 - �ּڰ� ã��
// �����̵� �˰����̶� ������ Ǯ��Ҵ�. �� ���� ���� Ǭ ���� �ƴϴ�. 
// cin.tie(0); �� ���� ������ �ð��ʰ��� �߻��ϴ� �ð� ������ ���� ���� �����̴�.
// ���׸�Ʈ Ʈ�� �˰����� ����ص� �ȴٴµ� ���� ��ȸ�� �ٸ� ������ �������...�� 
#include <iostream>
#include <deque>
using namespace std;

typedef pair<int, int> pii;

int arr[5000000];
int N, L;
deque<pii> dq;

int main() {
	// cin�� �Է¼ӵ��� ���. 
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	// �Է� �ޱ�. 
	cin >> N >> L;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	// �����̵� �˰���.  
	for (int i = 0; i < N; i++) {
		// idx�� ���� dq�� front idx�� i - L �� �� pop�� �Ѵ�. 
		if (!dq.empty() && dq.front().second <= i - L) dq.pop_front();
		// �̹� ����ִ� ���� �� pop�� �� �� �ִ�.
		// ������ �̹� �ݺ����� �߰��� arr[i] ���� ������ �ִ� ���� ���� ������ �翬�� ���� ū ������ ��� �ȴ�.
		// �׷��� ū ������ ��� pop���ָ� �ڿ������� dq�� �������� ���ķ� ������ �޾�����. 
		while (!dq.empty() && dq.back().first > arr[i]) dq.pop_back();
		// ���� push �� ���. 
		dq.push_back(pii(arr[i], i));
		cout << dq.front().first << " ";
	}
	
	return 0;
} 
