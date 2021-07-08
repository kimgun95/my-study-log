// 2096 - 내려가기.
// 처음엔 단순하게 2중 for문으로 구현하여 시간 초과가 발생했고.
// dp를 이용하면 좀 더 빨라지지 않을까 했는데 이때는 메모리 초과가 발생했다.
// int가 4byte이니 백만크기의 배열을 사용하면 4MB를 쓰는 격이다.
// 내가 num, max_dp, min_dp를 각각 30만씩 사용을 해서 메모리 초과가 발생한 것 같다. 근사하게 넘은건가...
// 해답을 보았는데 너무 단순해서 충격이었다. 그냥 입력을 받는대로 dp에 최솟값, 최댓값을 계산해서 넣으면 되었던 것... ㅠ 
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
