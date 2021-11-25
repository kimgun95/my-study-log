// 2096 - ��������.
// ó���� �ܼ��ϰ� 2�� for������ �����Ͽ� �ð� �ʰ��� �߻��߰�.
// dp�� �̿��ϸ� �� �� �������� ������ �ߴµ� �̶��� �޸� �ʰ��� �߻��ߴ�.
// int�� 4byte�̴� �鸸ũ���� �迭�� ����ϸ� 4MB�� ���� ���̴�.
// ���� num, max_dp, min_dp�� ���� 30���� ����� �ؼ� �޸� �ʰ��� �߻��� �� ����. �ٻ��ϰ� �����ǰ�...
// �ش��� ���Ҵµ� �ʹ� �ܼ��ؼ� ����̾���. �׳� �Է��� �޴´�� dp�� �ּڰ�, �ִ��� ����ؼ� ������ �Ǿ��� ��... �� 
#include <iostream>
using namespace std;

int N;
int num[3];
int max_dp[3] = {0,};
int min_dp[3] = {0,};
int min_val;
int max_val;


int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		
		cin >> num[0] >> num[1] >> num[2];
		
		int temp[3];
		temp[0] = max_dp[0];
		temp[1] = max_dp[1];
		temp[2] = max_dp[2];
		
		max_dp[0] = max(temp[0], temp[1]) + num[0];
		max_dp[1] = max(max(temp[0], temp[1]), temp[2]) + num[1];	
		max_dp[2] = max(temp[1], temp[2]) + num[2];
		
		temp[0] = min_dp[0];
		temp[1] = min_dp[1];
		temp[2] = min_dp[2];
		
		min_dp[0] = min(temp[0], temp[1]) + num[0];
		min_dp[1] = min(min(temp[0], temp[1]), temp[2]) + num[1];	
		min_dp[2] = min(temp[1], temp[2]) + num[2];
		
	}
	
	max_val = max(max(max_dp[0], max_dp[1]), max_dp[2]);
	min_val = min(min(min_dp[0], min_dp[1]), min_dp[2]);
	
	cout << max_val << " " << min_val;
	
	return 0;
} 
