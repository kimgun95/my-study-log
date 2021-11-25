// 2805 - �����ڸ��� 
// �ܼ��� ��� ������ ��� ���̷� �ڸ����� �ߴٰ�  �ð��ʰ��� �߻��ߴ�.
// �̺�Ž���� �ؾ� �߰� ������ ���� �� Ʋ�ȴٴ� �亯�� �޾Ҵµ�. ������ �ڷ��� �����̴�.
// ���ǿ��� ���� ���̰� 20�� ���Ϸ� ������ �־ int�� �ذ��� �ǰ��� �ߴµ�.
// �Ʒ� ���Ŀ��� mid����̳� cnt��� ����� int �ڷ��� ũ�⸦ �Ѵ� ���� ���� �� �־ long�� �ٲ��־���. 
#include <iostream>
#include <algorithm>
using namespace std;

long N, M;
long tree[1000000];
long highest = 0;
long ans = 0;
long mid;

void cut(long low, long high) {
	mid = (low + high) / 2;
	long cnt = 0;
	
	if (low > high) return;
	
	for (int i = N - 1; i >= 0; i--) {
		if (tree[i] - mid < 0) break;
		cnt += tree[i] - mid;
	}
	
	if (cnt >= M) ans = max(ans, mid);
	
	if (cnt < M) cut(low, mid - 1);
	else if (cnt > M) cut(mid + 1, high);
	return;
}
	


int main() {
	// �Է� �ޱ�. 
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> tree[i];
		if (tree[i] > highest) highest = tree[i];
	}
	sort(tree, tree + N);
	
	cut(0, highest);
	cout << ans;
	return 0;
} 
