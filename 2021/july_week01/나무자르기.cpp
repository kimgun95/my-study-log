// 2805 - 나무자르기 
// 단순히 모든 나무를 모든 길이로 자르려고 했다가  시간초과가 발생했다.
// 이분탐색을 해야 했고 마지막 제출 때 틀렸다는 답변을 받았는데. 이유는 자료형 때문이다.
// 조건에서 나무 길이가 20억 이하로 조건이 있어서 int로 해결이 되겠지 했는데.
// 아래 수식에서 mid계산이나 cnt계산 결과로 int 자료형 크기를 넘는 값을 받을 수 있어서 long로 바꿔주었다. 
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
	// 입력 받기. 
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
