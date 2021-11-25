// 11003 - 최솟값 찾기
// 슬라이딩 알고리즘이란 것으로 풀어보았다. 아 물론 내가 푼 것이 아니다. 
// cin.tie(0); 를 넣지 않으면 시간초과가 발생하는 시간 제한이 아주 빡센 문제이다.
// 세그먼트 트리 알고리즘을 사용해도 된다는데 다음 기회에 다른 문제로 배워보자...ㅎ 
#include <iostream>
#include <deque>
using namespace std;

typedef pair<int, int> pii;

int arr[5000000];
int N, L;
deque<pii> dq;

int main() {
	// cin의 입력속도를 향상. 
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	// 입력 받기. 
	cin >> N >> L;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	// 슬라이딩 알고리즘.  
	for (int i = 0; i < N; i++) {
		// idx를 통해 dq의 front idx가 i - L 이 면 pop을 한다. 
		if (!dq.empty() && dq.front().second <= i - L) dq.pop_front();
		// 이미 들어있는 값을 왜 pop해 할 수 있다.
		// 어차피 이번 반복문에 추가할 arr[i] 값이 기존에 있는 값들 보다 작으면 당연히 앞의 큰 값들은 없어도 된다.
		// 그렇게 큰 값들을 모두 pop해주면 자연스럽게 dq는 오름차순 정렬로 값들이 받아진다. 
		while (!dq.empty() && dq.back().first > arr[i]) dq.pop_back();
		// 값을 push 및 출력. 
		dq.push_back(pii(arr[i], i));
		cout << dq.front().first << " ";
	}
	
	return 0;
} 
