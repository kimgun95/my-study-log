// 2003 - ������ ��2
// ���� Ǯ����...! �ܼ��� for�� 2���� �̿��Ͽ� �ذ��� ������� ���� ����..! 
#include <iostream>
#include <vector>
using namespace std;

int N, M;
int num[30000]; // ���ڵ��� �Է� ����. 
vector<int> arr; // M���� ���� ���ڵ��� idx�� ����. 
int ans = 0; // ����� ��� ����. 

// ���ؼ� M�� �Ǵ� ����� ���� ã�´�. 
void find() {
	// arr�� �ִ� ���ڵ�θ� Ž���� ����. 
	for (int i = 0; i < arr.size(); i++) {
		int number = 0;
		// ���� ���ڵ��� ���ϸ鼭 M�� �Ǵ��� Ȯ��. 
		for (int j = arr[i]; j < N; j++) {
			number += num[j];
			if (number == M) {
				ans += 1;
				break;
			} else if (number > M) break;
		}
	}
	return;
}


int main() {
	// �Է� �ޱ�. 
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
		// M���� ���� ���ڵ��� idx�� �̸� �����Ѵ�. (Ž�� ������ �� �� �����Ű�� ����) 
		if (num[i] <= M) {
			arr.push_back(i);
		} 
	}
	
	find();
	cout << ans;
	
	return 0;
} 
