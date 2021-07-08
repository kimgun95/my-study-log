// 7453 - 합이 0인 네 정수
// 솔직히 어떤 방향으로 할지 몰랐는데 이전에 풀었던 두 배열의 합과 같은 흐름이었다.
// 이번에는 4개의 배열로 갯수만 많아진 것. 2개 배열씩 짝지어서 경우의 수 vector를 만들어준다.
// 한 쪽 vector은 sort를 한 뒤 다른 vector의 경우의 수에 -1을 한 값이 있는지 upper_bound, lower_bound로 찾아준다.
// 틀렸습니다. 가 나왔었는데 이는 ans의 자료형을 int로 해서... long long으로 바꾸니 해결.
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int A[4000], B[4000], C[4000], D[4000];
vector<int> x, y;
long long ans = 0;

int main() {
	// 입력 받기. 
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> A[i] >> B[i] >> C[i] >> D[i];
	}	
	
	
	// A,B가 합해서 나오는 경우, C,D가 합해서 나오는 경우 생성 
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			x.push_back(A[i] + B[j]);
			y.push_back(C[i] + D[j]);
		}
	}
	
	sort(y.begin(), y.end());
	 
	for (auto num : x) {
		
		int find = num * -1;
		ans += upper_bound(y.begin(), y.end(), find) - lower_bound(y.begin(), y.end(), find);
	}
	cout << ans;
	
	return 0;
} 
