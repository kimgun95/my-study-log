// 7453 - ���� 0�� �� ����
// ������ � �������� ���� �����µ� ������ Ǯ���� �� �迭�� �հ� ���� �帧�̾���.
// �̹����� 4���� �迭�� ������ ������ ��. 2�� �迭�� ¦��� ����� �� vector�� ������ش�.
// �� �� vector�� sort�� �� �� �ٸ� vector�� ����� ���� -1�� �� ���� �ִ��� upper_bound, lower_bound�� ã���ش�.
// Ʋ�Ƚ��ϴ�. �� ���Ծ��µ� �̴� ans�� �ڷ����� int�� �ؼ�... long long���� �ٲٴ� �ذ�.
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int A[4000], B[4000], C[4000], D[4000];
vector<int> x, y;
long long ans = 0;

int main() {
	// �Է� �ޱ�. 
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> A[i] >> B[i] >> C[i] >> D[i];
	}	
	
	
	// A,B�� ���ؼ� ������ ���, C,D�� ���ؼ� ������ ��� ���� 
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			x.push_back(A[i] + B[j]);
			y.push_back(C[i] + D[j]);
		}
	}
	
	sort(y.begin(), y.end());
	 
	for (auto num : x) {
		
		int find = num * -1;
		ans += upper_bound(y.begin(), y.end(), find) - lower_bound(y.begin(), y.end(), find);
	}
	cout << ans;
	
	return 0;
} 
