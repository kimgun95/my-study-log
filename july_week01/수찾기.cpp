// 1920 - 수 찾기 
// 간단한 문제이기에 당연히 최적화 관련 문제일거라 생각했고 역시 맞았다.
// 단순하게 완전탐색을 하면 안되고 이분탐색으로 속도 향상을 시켰다. 
// 마지막에 endl 때문에 시간초과가 발생하여 잠깐 당황했었다. 
#include <iostream>
#include <algorithm> 
using namespace std;

#define MAX (1000000)
int N, M;
int A[MAX], B[MAX];
int l, r, mid;

int main() {
	// 아래 코드가 속도 개선에 도움을 주는데 문제 해결에는 영향이 없었다. 
	//ios_base::sync_with_stdio(0);cin.tie(0);
	
	// 입력 받기. 
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> B[i];
	}
	
	// A 배열을 정렬 후 탐색하는 게 편하기 때문에 sort 
	sort(A, A + N);
	
	// M개의 숫자에 대해 테스트. 
	for (int i = 0; i < M; i++) {
		l = 0;
		r = N - 1;
		int check = 0;
		// 이분 탐색을 진행하였다. 
		while (l <= r) {
			mid = (l + r) / 2;
			if (A[mid] == B[i]) {
				check = 1;
				break;
			} else if (B[i] < A[mid]) {
				r = mid - 1;
			} else {
				l = mid + 1;
			}
		}
		// 결과 출력. 이때 여기서 시간초과가 발생 했었다. 이유는 endl 때문. \n을 사용이 좀 더 빠르다. 
		if (check == 1) cout << 1 << "\n";
		else cout << 0 << "\n";
	}
} 
