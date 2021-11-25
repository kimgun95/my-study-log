// 2143 - �� �迭�� ��
// Ǯ�ٰ� ������ ���̵� �ȳ��Դ�. 
// vector�� upper_bound, lower_bound�� �����ϰ� �̿��ϸ� �ƴ�.
// ��� ��츦 ã�Ƽ� vector�� ���� ���� �� �Լ��� Ȱ���ϸ� ��ġ�� �˾Ƽ� ã�Ƴ��༭ ���� ����̴�...
// for �ݺ������� auto�� dev c++���� ������ �ȵǴµ�  "-std=c++11" �� �����Ϸ��� �߰��Ͽ� �ذ��ߴ�. 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int n, m;
int A[1000], B[1000];
vector<int> A_res, B_res;
long ans = 0;

// A�� B�� �ι迭�� �� ��� ��츦 ��� �Ͽ� vector�� push_back 
void make_num() {
	for (int i = 0; i < n; i++) {
		int number = 0;
		for (int j = i; j < n; j++) {
			number += A[j];
			A_res.push_back(number);
		}
	}
	for (int i = 0; i < m; i++) {
		int number = 0;
		for (int j = i; j < m; j++) {
			number += B[j];
			B_res.push_back(number);
		}
	}
	return;
}

int main() {
	// �Է� �ޱ�. 
	cin >> T;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> A[i];
	}	
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> B[i];
	}
	
	// �ι迭�� �� ��� ��� �� �� 
	make_num();
	// �ڿ��� ����� ���� ����� �������� ���� B_res�� sort 
	sort(B_res.begin(), B_res.end());
	
	// A_res�� �ִ� �� �� �߿� �ߺ��� �־ ó���� �ƴ��� �ʳ�? �ߴµ� ���ڸ��� ������� ������ �ٸ��� ������ ������. 
	for (auto num : A_res) {
		int diff = T - num;
		// upper_bound�� lower_bound ��� iterator�� ��ȯ�ϸ� �� �� ���� ���� ���� ���� �޾Ƴ���. 
		ans += upper_bound(B_res.begin(), B_res.end(), diff) - lower_bound(B_res.begin(), B_res.end(), diff);
	}
	cout << ans;
	
	
	return 0;
} 
