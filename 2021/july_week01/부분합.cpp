//1806 - �κ���.
// �ð����⵵�� �ذ� ���ؼ� Ʋ�ȴ�. ���� �ܼ��� O(N^2)���� �ذ��� �Ϸ� �߰�... �翬�� Ʋ������ O(N)���� ������ �ߴ�.
// ���⼭�� �� ������ �˰����� ���Ǿ��� �ϳ��� �迭�� ������ 2���� ����ؼ� �ݺ��� �ϳ��� ������ �ذ��ϴ� ���̴�.
// start, end 2�� �����͸� �̿��� end�� �÷����� ���� ���� S���� ũ�� ����� ������ٸ� start�� �ϳ� �÷� ���ο� ���� ã�ư��� ���̴�. 
#include <iostream>
using namespace std;

int N, S;
int num[100000]; // ���ڵ��� �迭�� ����. 
int ans = 100001; // ����� ��� ����. 

void cal() {
	int start = 0, end = 0, sum = 0;
	// end�� N���� �� ������ �ݺ��ϸ� �ȴ�. ��·�� �ݺ��� �ϳ� ���..! 
	while (start <= end) {
		if (sum >= S) {	// sum�� s���� ũ�ų� ������ ans�� ���. 
			ans = min(ans,end - start);	
			sum -= num[start++]; // start ��ġ�� �ϳ� �������� ���ο� sum���� �����. �ٽ� S���� Ŀ�� ������ �ݺ��� ������ ��. 
		}
		else if (end == N) break; // break ����. 
		else sum += num[end++];	// sum�� ���ڸ� �ϳ��� ��� ����.
	}
	return;
}

int main() {
	cin >> N >> S;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}
	
	cal();
	
	if (ans == 100001) cout << 0;
	else cout << ans;
	
	
	return 0;
} 
