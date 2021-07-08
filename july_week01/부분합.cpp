//1806 - 부분합.
// 시간복잡도를 해결 못해서 틀렸다. 나는 단순히 O(N^2)으로 해결을 하려 했고... 당연히 틀렸으니 O(N)으로 만들어야 했다.
// 여기서는 투 포인터 알고리즘이 사용되었고 하나의 배열에 포인터 2개를 사용해서 반복문 하나로 문제를 해결하는 식이다.
// start, end 2개 포인터를 이용해 end를 늘려가며 더한 값이 S보다 크게 만들고 만들었다면 start를 하나 늘려 새로운 것을 찾아가는 식이다. 
#include <iostream>
using namespace std;

int N, S;
int num[100000]; // 숫자들을 배열에 저장. 
int ans = 100001; // 출력할 결과 저장. 

void cal() {
	int start = 0, end = 0, sum = 0;
	// end가 N으로 갈 때까지 반복하면 된다. 어쨌든 반복문 하나 사용..! 
	while (start <= end) {
		if (sum >= S) {	// sum이 s보다 크거나 같을때 ans값 계산. 
			ans = min(ans,end - start);	
			sum -= num[start++]; // start 위치를 하나 증가시켜 새로운 sum값을 만든다. 다시 S보다 커질 때까지 반복문 진행할 것. 
		}
		else if (end == N) break; // break 조건. 
		else sum += num[end++];	// sum에 숫자를 하나씩 계속 저장.
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
