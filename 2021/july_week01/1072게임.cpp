// 1072 - ����
// ���� �ð��ʰ�, Ʋ�Ƚ��ϴ� �� �����淡 �ڷ��� ũ�� �������� �˾Ҵ�.
// ������ long long���� �ڷ����� �θ� �ʰ��� ���� �߻����� �ʾƼ� ������������.
// �켱 -1�� ���� �� �ִ� ������ �·��� 99�� ���� �ִٴ� ���̴�.
// �·��� 99���� ���� 100���� ���� �� ����. ó�� �˾Ҵ�...���� ���� �� �ȵ�.
// �׸��� �̺� Ž���� �ؾ��ߴ�. �� 10������ �� �Ѵٰ� �����ϰ� ���⼭ �̺�Ž���� ���� Ȯ���� �ٻ��� ���� ã���� �ȴ�. 
#include <iostream>
using namespace std;

long long X, Y;
int start = 0;
int last = 1000000000;
int mid;
int ans = 0;

int main() {
	cin >> X >> Y;
	
	int res;
	res = (Y * 100) / X;
	
	if (X == Y || res >= 99) {
		cout << -1;
		return 0;
	}

	while (start <= last) {
		mid = (start + last) / 2;
		
		int win = ((Y + mid) * 100) / (X + mid);
		if (res >= win) {
			
			start = mid + 1;
		} else {
			ans = mid;
			last = mid - 1;
		}
	}
	cout << ans;
	return 0;
}
