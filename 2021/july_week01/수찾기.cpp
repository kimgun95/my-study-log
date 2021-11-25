// 1920 - �� ã�� 
// ������ �����̱⿡ �翬�� ����ȭ ���� �����ϰŶ� �����߰� ���� �¾Ҵ�.
// �ܼ��ϰ� ����Ž���� �ϸ� �ȵǰ� �̺�Ž������ �ӵ� ����� ���״�. 
// �������� endl ������ �ð��ʰ��� �߻��Ͽ� ��� ��Ȳ�߾���. 
#include <iostream>
#include <algorithm> 
using namespace std;

#define MAX (1000000)
int N, M;
int A[MAX], B[MAX];
int l, r, mid;

int main() {
	// �Ʒ� �ڵ尡 �ӵ� ������ ������ �ִµ� ���� �ذῡ�� ������ ������. 
	//ios_base::sync_with_stdio(0);cin.tie(0);
	
	// �Է� �ޱ�. 
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> B[i];
	}
	
	// A �迭�� ���� �� Ž���ϴ� �� ���ϱ� ������ sort 
	sort(A, A + N);
	
	// M���� ���ڿ� ���� �׽�Ʈ. 
	for (int i = 0; i < M; i++) {
		l = 0;
		r = N - 1;
		int check = 0;
		// �̺� Ž���� �����Ͽ���. 
		while (l <= r) {
			mid = (l + r) / 2;
			if (A[mid] == B[i]) {
				check = 1;
				break;
			} else if (B[i] < A[mid]) {
				r = mid - 1;
			} else {
				l = mid + 1;
			}
		}
		// ��� ���. �̶� ���⼭ �ð��ʰ��� �߻� �߾���. ������ endl ����. \n�� ����� �� �� ������. 
		if (check == 1) cout << 1 << "\n";
		else cout << 0 << "\n";
	}
} 
